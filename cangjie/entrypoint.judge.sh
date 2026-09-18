#!/bin/sh
set -ex

rm -rf /judger/*
mkdir -p /judger/run /judger/spj

chown compiler:code /judger/run
chmod 711 /judger/run

chown compiler:spj /judger/spj
chmod 710 /judger/spj

CPU_CORE_NUM="$(nproc)"
if [ "$CPU_CORE_NUM" -lt 2 ]; then
    export WORKER_NUM=2;
else
    export WORKER_NUM="$CPU_CORE_NUM";
fi

# Recurring heartbeat: the stock image ships no scheduler, so the judge never
# registers with the backend on its own. Background a loop that posts the
# heartbeat (via the venv python, which has `requests`) every 10s.
if [ -z "$DISABLE_HEARTBEAT" ]; then
    (
        cd /app
        while true; do
            /app/.venv/bin/python /app/service.py >> /log/heartbeat.log 2>&1 || true
            sleep 10
        done
    ) &
fi

exec .venv/bin/gunicorn server:app --workers $WORKER_NUM --threads 4 --error-logfile /log/gunicorn.log --bind 0.0.0.0:8080
