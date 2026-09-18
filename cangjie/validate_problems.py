#!/usr/bin/env python3
"""Independently verify every (stdin, expected_stdout) case in problems_data.py.
Recomputes the answer with a reference solver keyed by _id. Reports mismatches."""
import sys, math
sys.path.insert(0, "cangjie")
from problems_data import PROBLEMS

def out(*vals):
    return " ".join(str(v) for v in vals) + "\n"

def solve(pid, inp):
    L = inp.split("\n")
    if pid == "HELLO":
        return "Hello, World!\n"
    if pid == "SUMN":
        n = int(L[0]); return out(n * (n + 1) // 2)
    if pid == "APLUSB":
        a, b = map(int, L[0].split()); return out(a + b)
    if pid == "MAXOF3":
        return out(max(map(int, L[0].split())))
    if pid == "STRREV":
        return out(L[0][::-1])
    if pid == "FACTORIAL":
        return out(math.factorial(int(L[0])))
    if pid == "FIBONACCI":
        n = int(L[0]); a, b = 0, 1
        for _ in range(n): a, b = b, a + b
        return out(a)
    if pid == "GCDLCM":
        a, b = map(int, L[0].split()); g = math.gcd(a, b); return out(g, a * b // g)
    if pid == "PRIMETEST":
        n = int(L[0])
        def isp(n):
            if n < 2: return False
            i = 2
            while i * i <= n:
                if n % i == 0: return False
                i += 1
            return True
        return out("Yes" if isp(n) else "No")
    if pid == "ARREXTREMES":
        arr = list(map(int, L[1].split())); return out(sum(arr), min(arr), max(arr))
    if pid == "PALINDROME":
        s = L[0]; return out("Yes" if s == s[::-1] else "No")
    if pid == "SORTINTS":
        arr = sorted(map(int, L[1].split())); return " ".join(map(str, arr)) + "\n"
    if pid == "VOWELCOUNT":
        s = L[0]; v = sum(c in "aeiou" for c in s); return out(v, len(s) - v)
    if pid == "BINSEARCH":
        n, k = map(int, L[0].split()); arr = list(map(int, L[1].split()))
        return out(arr.index(k) if k in arr else -1)
    if pid == "MATRIXTRANS":
        r, c = map(int, L[0].split()); m = [list(map(int, L[1 + i].split())) for i in range(r)]
        return "".join(" ".join(str(m[i][j]) for i in range(r)) + "\n" for j in range(c))
    if pid == "PARENMATCH":
        s = L[0]; pairs = {")": "(", "]": "[", "}": "{"}; st = []
        ok = True
        for ch in s:
            if ch in "([{": st.append(ch)
            elif ch in pairs:
                if not st or st.pop() != pairs[ch]: ok = False; break
        ok = ok and not st
        return out("Valid" if ok else "Invalid")
    if pid == "MAXSUBARR":
        arr = list(map(int, L[1].split())); best = cur = arr[0]
        for x in arr[1:]: cur = max(x, cur + x); best = max(best, cur)
        return out(best)
    if pid == "COINCHANGE":
        n, m = map(int, L[0].split()); coins = list(map(int, L[1].split()))
        INF = float("inf"); dp = [0] + [INF] * m
        for a in range(1, m + 1):
            for c in coins:
                if c <= a and dp[a - c] + 1 < dp[a]: dp[a] = dp[a - c] + 1
        return out(dp[m] if dp[m] != INF else -1)
    if pid == "LCS":
        s, t = L[0], L[1]; dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                dp[i][j] = dp[i-1][j-1] + 1 if s[i-1] == t[j-1] else max(dp[i-1][j], dp[i][j-1])
        return out(dp[len(s)][len(t)])
    if pid == "KNAPSACK01":
        n, w = map(int, L[0].split()); items = [tuple(map(int, L[1 + i].split())) for i in range(n)]
        dp = [0] * (w + 1)
        for wt, val in items:
            for c in range(w, wt - 1, -1): dp[c] = max(dp[c], dp[c - wt] + val)
        return out(max(dp))
    if pid == "TWOSUM":
        n, target = map(int, L[0].split()); arr = list(map(int, L[1].split()))
        seen = {}
        for i, x in enumerate(arr):
            if target - x in seen: return out(seen[target - x], i)
            seen[x] = i
        return out(-1)
    if pid == "CLIMBSTAIRS":
        n = int(L[0])
        if n <= 2: return out(n)
        a, b = 1, 2
        for _ in range(3, n + 1): a, b = b, a + b
        return out(b)
    if pid == "FIZZBUZZ":
        n = int(L[0]); res = []
        for i in range(1, n + 1):
            if i % 15 == 0: res.append("FizzBuzz")
            elif i % 3 == 0: res.append("Fizz")
            elif i % 5 == 0: res.append("Buzz")
            else: res.append(str(i))
        return " ".join(res) + "\n"
    if pid == "VALIDANAG":
        s, t = L[0], L[1]; return out("Yes" if sorted(s) == sorted(t) else "No")
    if pid == "STOCKPROFIT":
        n = int(L[0]); prices = list(map(int, L[1].split()))
        min_p = float("inf"); max_p = 0
        for p in prices:
            if p < min_p: min_p = p
            if p - min_p > max_p: max_p = p - min_p
        return out(max_p)
    if pid == "LONGESTSUBSTR":
        s = L[0]; last = {}; left = max_len = 0
        for i, ch in enumerate(s):
            if ch in last and last[ch] >= left: left = last[ch] + 1
            last[ch] = i
            max_len = max(max_len, i - left + 1)
        return out(max_len)
    if pid == "MERGEINTERVALS":
        n = int(L[0]); intervals = [list(map(int, L[1 + i].split())) for i in range(n)]
        intervals.sort(key=lambda x: x[0])
        merged = []
        for s, e in intervals:
            if not merged or merged[-1][1] < s: merged.append([s, e])
            else: merged[-1][1] = max(merged[-1][1], e)
        return "".join(f"{s} {e}\n" for s, e in merged)
    if pid == "ROTIMG":
        n = int(L[0]); m = [list(map(int, L[1 + i].split())) for i in range(n)]
        rot = [[m[n - 1 - j][i] for j in range(n)] for i in range(n)]
        return "".join(" ".join(str(rot[i][j]) for j in range(n)) + "\n" for i in range(n))
    if pid == "TRAPPINGRAIN":
        n = int(L[0]); h = list(map(int, L[1].split()))
        left, right = 0, n - 1; left_max = right_max = water = 0
        while left < right:
            if h[left] < h[right]:
                if h[left] >= left_max: left_max = h[left]
                else: water += left_max - h[left]
                left += 1
            else:
                if h[right] >= right_max: right_max = h[right]
                else: water += right_max - h[right]
                right -= 1
        return out(water)
    if pid == "LIS":
        import bisect
        n = int(L[0]); arr = list(map(int, L[1].split()))
        tails = []
        for x in arr:
            idx = bisect.bisect_left(tails, x)
            if idx == len(tails): tails.append(x)
            else: tails[idx] = x
        return out(len(tails))
    return None

bad = 0; total = 0
for p in PROBLEMS:
    pid = p["_id"]
    for i, (inp, exp) in enumerate(p["cases"], 1):
        total += 1
        got = solve(pid, inp)
        if got is None:
            print(f"[NO-SOLVER] {pid}"); bad += 1; break
        if got != exp:
            bad += 1
            print(f"[MISMATCH] {pid} case {i}: input={inp!r} expected={exp!r} got={got!r}")
print(f"\n{total} cases checked, {bad} mismatches")
sys.exit(1 if bad else 0)
