import time
from problem.models import Problem
from account.models import User
from submission.models import Submission, JudgeStatus

admin = User.objects.get(username="root")
S = {v: k for k, v in JudgeStatus.__dict__.items() if isinstance(v, int)}


def submit_bare(pid, body):
    p = Problem.objects.get(_id=pid)
    s = Submission.objects.create(problem=p, user_id=admin.id, username=admin.username,
                                  language="Cangjie", code=body, contest=None)
    from judge.tasks import judge_task
    judge_task(s.id, p.id)
    for _ in range(25):
        s.refresh_from_db()
        if s.result not in (JudgeStatus.PENDING, JudgeStatus.JUDGING):
            break
        time.sleep(1)
    print(pid, "->", s.result, S.get(s.result))
    Submission.objects.filter(id=s.id).delete()


# Bare function bodies only (what the user types in the editor)
submit_bare("HELLO", 'func solve(): String {\n    return "Hello, World!"\n}')
submit_bare("SUMN", "func sumToN(n: Int64): Int64 {\n    return n * (n + 1) / 2\n}")
submit_bare("APLUSB", "func add(a: Int64, b: Int64): Int64 {\n    return a + b\n}")

submit_bare("PRIMETEST", """func isPrime(n: Int64): Bool {
    if (n < 2) { return false }
    var i = 2
    while (i * i <= n) {
        if (n % i == 0) { return false }
        i++
    }
    return true
}""")

submit_bare("LCS", """func lcs(s: String, t: String): Int64 {
    let a = s.toArray()
    let b = t.toArray()
    let n = a.size
    let m = b.size
    let dp = Array<Array<Int64>>(n + 1, {_ => Array<Int64>(m + 1, {_ => 0})})
    var i = 1
    while (i <= n) {
        var j = 1
        while (j <= m) {
            if (a[i-1] == b[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1
            } else {
                dp[i][j] = if (dp[i-1][j] > dp[i][j-1]) { dp[i-1][j] } else { dp[i][j-1] }
            }
            j++
        }
        i++
    }
    return dp[n][m]
}""")
