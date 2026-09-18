# OnlineJudge + Cangjie (QingdaoU OJ, self-hosted)

A LeetCode-style online judge (QingdaoU OnlineJudge 2.0) with **Cangjie 1.0.5**
added as a submission language, on top of the stock C / C++ / Java / Python3 /
Go / JavaScript.

## What's custom here

Everything Cangjie-specific lives in `cangjie/` and is wired into
`docker-compose.yml` via `build:` directives, so a plain `up -d --build`
reproduces the images from source — no private image registry required.

| File | Purpose |
|------|---------|
| `cangjie/Dockerfile.judge` | Judge image + Cangjie SDK (`COPY --from zxilly/cangjie`), `chmod a+rX /opt/cangjie` so the sandbox `compiler`/`code` users can run `cjc`, plus a heartbeat entrypoint. |
| `cangjie/entrypoint.judge.sh` | Stock judge entrypoint + a background loop that posts the judge heartbeat every 10s (stock image ships no scheduler, so it otherwise never registers). |
| `cangjie/Dockerfile.backend` | Backend image with the Cangjie entry appended to `judge/languages.py`. |
| `cangjie/languages_cangjie.py` | The Cangjie language config (compile/run command, env, `seccomp_rule=None`, unlimited compile memory). |

### Why these specific fixes

- **`chmod -R a+rX /opt/cangjie`** — the upstream Cangjie SDK ships `0750`
  owned by `1001:users`; the judge compiles as user `compiler` (uid 901) and
  runs as `code`, neither of which could otherwise execute `cjc`.
- **`max_memory: -1` for compile** — `cjc` spawns worker threads that reserve
  virtual address space; a bounded rlimit makes thread creation fail. Java's
  compile uses `-1` for the same reason.
- **`seccomp_rule: None` for run** — the Cangjie runtime does its own
  threading/`mmap`/`futex`; strict syscall allowlists would kill it. Same
  approach the stock config uses for Java.

## Environment notes (rootless Podman / SELinux)

The compose volumes carry `:U,z` flags:
- `:z` — SELinux relabel so containers can read/write host bind mounts
  (required on Enforcing systems; harmless elsewhere).
- `:U` — chown the bind mount into the container user namespace (rootless).

Ports are mapped to **8080/8443** instead of 80/443 because rootless Podman
cannot bind privileged ports. On a root Docker host you can change these back
to `80:8000` / `443:1443`.

The judge and backend share a secret via `TOKEN` (judge) and
`JUDGE_SERVER_TOKEN` (backend) — **change `CangjieOJToken2026` before any real
deployment.**

## Deploy

```bash
git clone <your-private-repo-url> oj && cd oj

# On a rootless-Podman + SELinux host: no changes needed.
# On a root Docker host: optionally switch ports back to 80/443 in
# docker-compose.yml and drop the :U flags (keep :z only if SELinux).

docker compose up -d --build      # or: podman-compose up -d
```

Wait ~1 minute for the backend to run DB migrations. Then:

- Frontend: `http://<host>:8080/`
- Admin: `http://<host>:8080/admin/` — default `root` / `rootroot`
  (**change immediately**).

Cangjie appears in the submission language dropdown automatically on first
boot (fresh DB). If you added Cangjie to an already-initialized DB, force a
re-seed of the languages option:

```bash
docker exec <postgres-container> psql -U onlinejudge -d onlinejudge \
  -c "DELETE FROM options_sysoptions WHERE key IN ('languages','spj_languages');"
docker restart <backend-container>
```

## Verifying Cangjie

Create a problem, allow the `Cangjie` language, and submit:

```cangjie
main() {
    println(1 + 2)
}
```

It should judge **Accepted**. (Verified locally end-to-end via the judge
dispatch pipeline.)
