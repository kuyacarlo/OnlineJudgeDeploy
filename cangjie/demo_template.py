import os, json, hashlib
from problem.models import Problem, ProblemRuleType
from account.models import User
from submission.models import Submission, JudgeStatus
from judge.tasks import judge_task

admin = User.objects.get(username="root")

cj_template = """//PREPEND BEGIN
import std.env.*
import std.convert.*
//PREPEND END
//TEMPLATE BEGIN
func add(a: Int64, b: Int64): Int64 {
    // write your code here
    return 0
}
//TEMPLATE END
//APPEND BEGIN
main() {
    let p = getStdIn().readln().getOrThrow().trimAscii().split(" ")
    println(add(Int64.parse(p[0]), Int64.parse(p[1])))
}
//APPEND END"""

TC = "/data/test_case/cjadd"
os.makedirs(TC, exist_ok=True)
cases = [("1 2\n", "3\n"), ("100 250\n", "350\n"), ("-5 5\n", "0\n")]
info = {"test_case_number": len(cases), "spj": False, "test_cases": {}}
score = []
for i, (inp, out) in enumerate(cases, 1):
    open(f"{TC}/{i}.in", "w").write(inp)
    open(f"{TC}/{i}.out", "w").write(out)
    info["test_cases"][str(i)] = {
        "stripped_output_md5": hashlib.md5(out.rstrip().encode()).hexdigest(),
        "input_size": len(inp.encode()), "output_size": len(out.encode()),
        "input_name": f"{i}.in", "output_name": f"{i}.out"}
    score.append({"input_name": f"{i}.in", "output_name": f"{i}.out", "score": 34})
open(f"{TC}/info", "w").write(json.dumps(info))

Problem.objects.filter(_id="CJADD").delete()
p = Problem.objects.create(
    _id="CJADD", title="A + B (function template demo)",
    description="Implement `add(a, b)` returning a+b. You write ONLY the function body.",
    input_description="Two space-separated ints", output_description="a+b",
    samples=[{"input": "1 2", "output": "3"}], test_case_id="cjadd",
    test_case_score=score, languages=["Cangjie"], template={"Cangjie": cj_template},
    created_by=admin, time_limit=5000, memory_limit=256,
    rule_type=ProblemRuleType.ACM, difficulty="Low", visible=True,
    io_mode={"io_mode": "Standard IO", "input": "input.txt", "output": "output.txt"},
    spj=False, source="demo", hint="")
print("CREATED CJADD, template langs:", list(p.template.keys()))

# Submit ONLY the function body -- no main(), no imports (LeetCode style)
user_code = "func add(a: Int64, b: Int64): Int64 {\n    return a + b\n}"
s = Submission.objects.create(problem=p, user_id=admin.id, username=admin.username,
                              language="Cangjie", code=user_code, contest=None)
judge_task(s.id, p.id)
s.refresh_from_db()
S = {v: k for k, v in JudgeStatus.__dict__.items() if isinstance(v, int)}
print("BARE-FUNCTION SUBMISSION ->", s.result, S.get(s.result))
Submission.objects.filter(id=s.id).delete()
