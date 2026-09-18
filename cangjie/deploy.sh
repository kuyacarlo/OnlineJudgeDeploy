#!/usr/bin/env bash
set -euo pipefail

echo "=== Deploying OnlineJudge with Cangjie Support ==="

# 1. Start containers with build
if command -v podman-compose >/dev/null 2>&1; then
    podman-compose up -d --build
elif command -v docker >/dev/null 2>&1 && docker compose version >/dev/null 2>&1; then
    docker compose up -d --build
else
    echo "Error: neither podman-compose nor docker compose found." >&2
    exit 1
fi

echo "Waiting for database and backend migrations (45s)..."
sleep 45

# 2. Seed problems and multi-language templates
echo "Seeding 30 problems with multi-language sample code..."
BACKEND_CID=$(podman ps -q --filter "name=oj-backend" 2>/dev/null || docker ps -q --filter "name=oj-backend")

if [ -z "$BACKEND_CID" ]; then
    echo "Error: oj-backend container not found running." >&2
    exit 1
fi

if command -v podman >/dev/null 2>&1; then
    podman cp cangjie/. "$BACKEND_CID:/tmp/"
    podman exec "$BACKEND_CID" python manage.py shell -c "import sys; sys.path.insert(0, '/tmp'); import seed_problems; import apply_templates"
else
    docker cp cangjie/. "$BACKEND_CID:/tmp/"
    docker exec "$BACKEND_CID" python manage.py shell -c "import sys; sys.path.insert(0, '/tmp'); import seed_problems; import apply_templates"
fi

echo "=== Deployment Complete ==="
echo "Access Frontend: http://<server-ip>:8080"
echo "Admin Panel:     http://<server-ip>:8080/admin (Default: root / rootroot)"
