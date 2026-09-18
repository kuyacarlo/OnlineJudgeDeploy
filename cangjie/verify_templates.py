#!/usr/bin/env python3
"""Verify Cangjie function-only templates end to end WITHOUT the OJ:
for each problem, assemble prepend+reference+append, compile with cjc inside the
judge container, run each test case, compare stdout (rstrip) to expected.

Run from repo root ON THE HOST; it shells into the judge container via podman.
"""
import re, subprocess, sys, json, base64, os
sys.path.insert(0, "cangjie")
from problems_data import PROBLEMS
from cangjie_templates import TEMPLATES
from reference_solutions import REFS

ALL_PROBLEMS = PROBLEMS

JUDGE = "onlinejudgedeploy_oj-judge_1"
LDP = "/opt/cangjie/runtime/lib/linux_x86_64_cjnative:/opt/cangjie/tools/lib"


def parse(tpl):
    prepend = re.findall(r"//PREPEND BEGIN\n([\s\S]+?)//PREPEND END", tpl)
    append = re.findall(r"//APPEND BEGIN\n([\s\S]+?)//APPEND END", tpl)
    return (prepend[0] if prepend else ""), (append[0] if append else "")


def run_in_judge(script):
    # pass script b64 to avoid quoting hell
    b = base64.b64encode(script.encode()).decode()
    cmd = ["podman", "exec", JUDGE, "sh", "-c",
           f"echo {b} | base64 -d | sh"]
    return subprocess.run(cmd, capture_output=True, text=True, timeout=120)


def verify(p):
    pid = p["_id"]
    if pid not in TEMPLATES or pid not in REFS:
        return pid, "SKIP (no template/ref)"
    prepend, append = parse(TEMPLATES[pid])
    full = f"{prepend}\n{REFS[pid]}\n{append}\n"
    full_b64 = base64.b64encode(full.encode()).decode()
    # build a shell script: write source, compile, then run each case
    lines = [
        "set -e",
        "d=$(mktemp -d)",
        "cd $d",
        f"echo {full_b64} | base64 -d > main.cj",
        f"export LD_LIBRARY_PATH={LDP}",
        "if ! /opt/cangjie/bin/cjc -O2 main.cj -o main 2>cerr; then echo COMPILE_FAIL; cat cerr; exit 3; fi",
    ]
    for i, (inp, _out) in enumerate(p["cases"]):
        ib = base64.b64encode(inp.encode()).decode()
        lines.append(f"if ! echo {ib} | base64 -d | ./main > out{i} 2>rerr; then echo RUN_FAIL_{i}; cat rerr; exit 4; fi")
    lines.append("echo ===OUTPUTS===")
    for i, _ in enumerate(p["cases"]):
        lines.append(f"echo ---CASE{i}---; cat out{i}")
    script = "\n".join(lines)
    r = run_in_judge(script)
    if "COMPILE_FAIL" in r.stdout or "COMPILE_FAIL" in r.stderr:
        return pid, "COMPILE_FAIL:\n" + (r.stdout + r.stderr)[:800]
    if "RUN_FAIL" in r.stdout:
        return pid, "RUN_FAIL:\n" + r.stdout[:800]
    # parse outputs
    parts = r.stdout.split("===OUTPUTS===")
    if len(parts) < 2:
        return pid, "NO_OUTPUT:\n" + (r.stdout + r.stderr)[:800]
    body = parts[1]
    got = re.split(r"---CASE\d+---\n", body)[1:]
    for i, (inp, exp) in enumerate(p["cases"]):
        g = got[i] if i < len(got) else ""
        if g.rstrip("\n").rstrip() != exp.rstrip("\n").rstrip():
            return pid, f"WRONG case{i}: in={inp!r} exp={exp!r} got={g!r}"
    return pid, "OK"


fails = 0
for p in ALL_PROBLEMS:
    pid, status = verify(p)
    mark = "OK " if status == "OK" else "XX "
    if status != "OK":
        fails += 1
    print(mark, pid, "" if status == "OK" else "-> " + status)
print(f"\n{'ALL TEMPLATES OK' if fails == 0 else str(fails) + ' TEMPLATE(S) FAILED'}")
sys.exit(1 if fails else 0)
