#!/usr/bin/env python
"""
Reusable problem seeder for QingdaoU OnlineJudge (run INSIDE the backend
container via:  python manage.py shell < cangjie/seed_problems.py).

Creates:
  - The Problem row with ACM rules, visible, multi-language support
  - Formatted hints with reference solutions in Cangjie, Python3, C, and C++
  - Editor starter templates for Cangjie, Python3, C, and C++
  - Complete on-disk test-case files with stripped_output_md5 checksums
"""
import os, json, hashlib, sys
from problem.models import Problem, ProblemRuleType
from account.models import User

ADMIN = User.objects.get(username="root")
TC_ROOT = "/data/test_case"
ALL_LANGS = ["Cangjie", "C", "C++", "Java", "Python3", "Golang", "JavaScript"]

try:
    from problems_data import PROBLEMS
    from sample_solutions import SAMPLE_SOLUTIONS
    from cangjie_templates import TEMPLATES
except ImportError:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, "/tmp")
    from problems_data import PROBLEMS
    from sample_solutions import SAMPLE_SOLUTIONS
    from cangjie_templates import TEMPLATES


def _md5_stripped(s: str) -> str:
    return hashlib.md5(s.rstrip().encode()).hexdigest()


def _write_cases(tc_id, cases):
    d = os.path.join(TC_ROOT, tc_id)
    os.makedirs(d, exist_ok=True)
    info = {"test_case_number": len(cases), "spj": False, "test_cases": {}}
    score = []
    per = max(1, 100 // len(cases))
    for i, (inp, out) in enumerate(cases, start=1):
        open(os.path.join(d, f"{i}.in"), "w").write(inp)
        open(os.path.join(d, f"{i}.out"), "w").write(out)
        info["test_cases"][str(i)] = {
            "stripped_output_md5": _md5_stripped(out),
            "input_size": len(inp.encode()), "output_size": len(out.encode()),
            "input_name": f"{i}.in", "output_name": f"{i}.out",
        }
        score.append({"input_name": f"{i}.in", "output_name": f"{i}.out", "score": per})
    open(os.path.join(d, "info"), "w").write(json.dumps(info))
    return score


def _format_hint(_id):
    sols = SAMPLE_SOLUTIONS.get(_id, {})
    if not sols:
        return ""
    sections = ["### Sample Solutions"]
    if "Cangjie" in sols:
        sections.append(f"#### Cangjie\n```cangjie\n{sols['Cangjie']}\n```")
    if "Python3" in sols:
        sections.append(f"#### Python 3\n```python\n{sols['Python3']}\n```")
    if "C" in sols:
        sections.append(f"#### C\n```c\n{sols['C']}\n```")
    if "C++" in sols:
        sections.append(f"#### C++\n```cpp\n{sols['C++']}\n```")
    return "\n\n".join(sections)


def _build_templates(_id):
    tpls = {}
    if _id in TEMPLATES:
        tpls["Cangjie"] = TEMPLATES[_id]
    return tpls


def seed(pdef):
    _id = pdef["_id"]
    Problem.objects.filter(_id=_id).delete()
    tc_id = _id.lower()
    score = _write_cases(tc_id, pdef["cases"])
    hint_md = _format_hint(_id)
    templates = _build_templates(_id)
    p = Problem.objects.create(
        _id=_id, title=pdef["title"], description=pdef["description"],
        input_description=pdef["input_description"],
        output_description=pdef["output_description"],
        samples=pdef["samples"], test_case_id=tc_id, test_case_score=score,
        languages=ALL_LANGS, template=templates, created_by=ADMIN,
        time_limit=5000, memory_limit=256, rule_type=ProblemRuleType.ACM,
        difficulty=pdef.get("difficulty", "Low"), visible=True,
        io_mode={"io_mode": "Standard IO", "input": "input.txt", "output": "output.txt"},
        spj=False, source="LeetCode / CSES", hint=hint_md,
    )
    print(f"CREATED {p._id} - {p.title} (Hint length: {len(hint_md)})")


if __name__ == "__main__" or True:
    for pdef in PROBLEMS:
        seed(pdef)
    print("TOTAL PROBLEMS IN DB:", Problem.objects.count())
