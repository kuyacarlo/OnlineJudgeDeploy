import time, sys
from problem.models import Problem
from account.models import User
from submission.models import Submission, JudgeStatus
from judge.tasks import judge_task

try:
    from sample_solutions import SAMPLE_SOLUTIONS
    from reference_solutions import REFS
except ImportError:
    sys.path.insert(0, "/tmp")
    from sample_solutions import SAMPLE_SOLUTIONS
    from reference_solutions import REFS

admin = User.objects.get(username="root")
S = {v: k for k, v in JudgeStatus.__dict__.items() if isinstance(v, int)}


def test_submit(pid, lang, code):
    p = Problem.objects.get(_id=pid)
    s = Submission.objects.create(
        problem=p, user_id=admin.id, username=admin.username,
        language=lang, code=code, contest=None
    )
    judge_task(s.id, p.id)
    for _ in range(30):
        s.refresh_from_db()
        if s.result not in (JudgeStatus.PENDING, JudgeStatus.JUDGING):
            break
        time.sleep(0.5)
    res_name = S.get(s.result, str(s.result))
    print(f"[{lang:8s}] {pid:15s} -> {res_name} (code {s.result})")
    Submission.objects.filter(id=s.id).delete()
    return s.result == 0


sample_tests = [
    ("HELLO", ["Cangjie", "Python3", "C", "C++"]),
    ("APLUSB", ["Cangjie", "Python3", "C", "C++"]),
    ("TWOSUM", ["Cangjie", "Python3", "C", "C++"]),
    ("FIZZBUZZ", ["Cangjie", "Python3", "C", "C++"]),
    ("STOCKPROFIT", ["Cangjie", "Python3", "C", "C++"]),
]

passed = 0
total = 0
for pid, langs in sample_tests:
    sols = SAMPLE_SOLUTIONS.get(pid, {})
    for lang in langs:
        code = REFS.get(pid) if lang == "Cangjie" and pid in REFS else sols.get(lang)
        if code:
            total += 1
            if test_submit(pid, lang, code):
                passed += 1

print(f"\n{passed}/{total} MULTI-LANGUAGE SUBMISSIONS ACCEPTED")

