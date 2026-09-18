"""Cangjie function-only templates, keyed by problem _id.

Each value is a full QDU template string with //PREPEND, //TEMPLATE, //APPEND
sections. On submit the judge assembles:  prepend + user_code + append.
The user edits ONLY the //TEMPLATE part (a function stub); the //APPEND main()
parses that problem's stdin format, calls the function, and prints the result.

Parsing helpers live in PREPEND so every append can use them.
"""

# Shared helpers injected via prepend for problems that need array/line parsing.
_HELPERS = """import std.env.*
import std.convert.*
import std.collection.*

func _rl(): String {
    return getStdIn().readln().getOrThrow().trimAscii()
}
func _ints(s: String): Array<Int64> {
    let r = ArrayList<Int64>()
    for (p in s.trimAscii().split(" ")) {
        if (p.size > 0) { r.add(Int64.parse(p)) }
    }
    return r.toArray()
}"""


def _tpl(prepend_body, template_body, append_body):
    return ("//PREPEND BEGIN\n" + prepend_body + "\n//PREPEND END\n"
            "//TEMPLATE BEGIN\n" + template_body + "\n//TEMPLATE END\n"
            "//APPEND BEGIN\n" + append_body + "\n//APPEND END")


TEMPLATES = {}

# HELLO: solve() -> String (no input)
TEMPLATES["HELLO"] = _tpl(
    _HELPERS,
    "func solve(): String {\n    // write your code here\n    return \"\"\n}",
    "main() {\n    println(solve())\n}")

# SUMN: sumToN(n) -> Int64  (single int)
TEMPLATES["SUMN"] = _tpl(
    _HELPERS,
    "func sumToN(n: Int64): Int64 {\n    // write your code here\n    return 0\n}",
    "main() {\n    println(sumToN(Int64.parse(_rl())))\n}")

# APLUSB: add(a,b)
TEMPLATES["APLUSB"] = _tpl(
    _HELPERS,
    "func add(a: Int64, b: Int64): Int64 {\n    // write your code here\n    return 0\n}",
    "main() {\n    let v = _ints(_rl())\n    println(add(v[0], v[1]))\n}")

# MAXOF3: maxOf3(a,b,c)
TEMPLATES["MAXOF3"] = _tpl(
    _HELPERS,
    "func maxOf3(a: Int64, b: Int64, c: Int64): Int64 {\n    // write your code here\n    return a\n}",
    "main() {\n    let v = _ints(_rl())\n    println(maxOf3(v[0], v[1], v[2]))\n}")

# STRREV: reverseString(s) -> String
TEMPLATES["STRREV"] = _tpl(
    _HELPERS,
    "func reverseString(s: String): String {\n    // write your code here\n    return s\n}",
    "main() {\n    println(reverseString(_rl()))\n}")

# FACTORIAL: factorial(n) -> Int64
TEMPLATES["FACTORIAL"] = _tpl(
    _HELPERS,
    "func factorial(n: Int64): Int64 {\n    // write your code here\n    return 1\n}",
    "main() {\n    println(factorial(Int64.parse(_rl())))\n}")

# FIBONACCI: fib(n) -> Int64
TEMPLATES["FIBONACCI"] = _tpl(
    _HELPERS,
    "func fib(n: Int64): Int64 {\n    // write your code here\n    return 0\n}",
    "main() {\n    println(fib(Int64.parse(_rl())))\n}")

# GCDLCM: gcdLcm(a,b) -> (Int64, Int64); print "g l"
TEMPLATES["GCDLCM"] = _tpl(
    _HELPERS,
    "func gcdLcm(a: Int64, b: Int64): (Int64, Int64) {\n    // return (gcd, lcm)\n    return (a, b)\n}",
    "main() {\n    let v = _ints(_rl())\n    let (g, l) = gcdLcm(v[0], v[1])\n    println(\"${g} ${l}\")\n}")

# PRIMETEST: isPrime(n) -> Bool; print Yes/No
TEMPLATES["PRIMETEST"] = _tpl(
    _HELPERS,
    "func isPrime(n: Int64): Bool {\n    // write your code here\n    return false\n}",
    "main() {\n    if (isPrime(Int64.parse(_rl()))) { println(\"Yes\") } else { println(\"No\") }\n}")

# ARREXTREMES: analyze(a) -> (sum,min,max)
TEMPLATES["ARREXTREMES"] = _tpl(
    _HELPERS,
    "func analyze(a: Array<Int64>): (Int64, Int64, Int64) {\n    // return (sum, min, max)\n    return (0, 0, 0)\n}",
    "main() {\n    _rl()\n    let a = _ints(_rl())\n    let (s, mn, mx) = analyze(a)\n    println(\"${s} ${mn} ${mx}\")\n}")

# PALINDROME: isPalindrome(s) -> Bool; print Yes/No
TEMPLATES["PALINDROME"] = _tpl(
    _HELPERS,
    "func isPalindrome(s: String): Bool {\n    // write your code here\n    return false\n}",
    "main() {\n    if (isPalindrome(_rl())) { println(\"Yes\") } else { println(\"No\") }\n}")

# SORTINTS: sortInts(a) -> Array<Int64>; print space-joined
TEMPLATES["SORTINTS"] = _tpl(
    _HELPERS,
    "func sortInts(a: Array<Int64>): Array<Int64> {\n    // write your code here\n    return a\n}",
    "main() {\n    _rl()\n    let a = sortInts(_ints(_rl()))\n    let sb = StringBuilder()\n    for (i in 0..a.size) {\n        if (i > 0) { sb.append(\" \") }\n        sb.append(a[i].toString())\n    }\n    println(sb.toString())\n}")

# VOWELCOUNT: countVC(s) -> (vowels, consonants)
TEMPLATES["VOWELCOUNT"] = _tpl(
    _HELPERS,
    "func countVC(s: String): (Int64, Int64) {\n    // return (vowels, consonants)\n    return (0, 0)\n}",
    "main() {\n    let (v, c) = countVC(_rl())\n    println(\"${v} ${c}\")\n}")

# MAXSUBARR: maxSubarray(a) -> Int64
TEMPLATES["MAXSUBARR"] = _tpl(
    _HELPERS,
    "func maxSubarray(a: Array<Int64>): Int64 {\n    // write your code here\n    return 0\n}",
    "main() {\n    _rl()\n    println(maxSubarray(_ints(_rl())))\n}")

# BINSEARCH: search(a, k) -> Int64 (index or -1)
TEMPLATES["BINSEARCH"] = _tpl(
    _HELPERS,
    "func search(a: Array<Int64>, k: Int64): Int64 {\n    // write your code here\n    return -1\n}",
    "main() {\n    let hdr = _ints(_rl())\n    let k = hdr[1]\n    let a = _ints(_rl())\n    println(search(a, k))\n}")

# COINCHANGE: minCoins(coins, m) -> Int64 (or -1)
TEMPLATES["COINCHANGE"] = _tpl(
    _HELPERS,
    "func minCoins(coins: Array<Int64>, m: Int64): Int64 {\n    // write your code here\n    return -1\n}",
    "main() {\n    let hdr = _ints(_rl())\n    let m = hdr[1]\n    let coins = _ints(_rl())\n    println(minCoins(coins, m))\n}")

# LCS: lcs(s, t) -> Int64
TEMPLATES["LCS"] = _tpl(
    _HELPERS,
    "func lcs(s: String, t: String): Int64 {\n    // write your code here\n    return 0\n}",
    "main() {\n    let s = _rl()\n    let t = _rl()\n    println(lcs(s, t))\n}")

# KNAPSACK01: knapsack(weights, values, W) -> Int64
TEMPLATES["KNAPSACK01"] = _tpl(
    _HELPERS,
    "func knapsack(weights: Array<Int64>, values: Array<Int64>, W: Int64): Int64 {\n    // write your code here\n    return 0\n}",
    "main() {\n    let hdr = _ints(_rl())\n    let n = hdr[0]\n    let W = hdr[1]\n    let ws = ArrayList<Int64>()\n    let vs = ArrayList<Int64>()\n    for (_ in 0..n) {\n        let row = _ints(_rl())\n        ws.add(row[0])\n        vs.add(row[1])\n    }\n    println(knapsack(ws.toArray(), vs.toArray(), W))\n}")

# PARENMATCH: isValid(s) -> Bool; print Valid/Invalid
TEMPLATES["PARENMATCH"] = _tpl(
    _HELPERS,
    "func isValid(s: String): Bool {\n    // write your code here\n    return false\n}",
    "main() {\n    if (isValid(_rl())) { println(\"Valid\") } else { println(\"Invalid\") }\n}")

# MATRIXTRANS: transpose(m, r, c) -> prints result itself is complex; give matrix + dims,
# function returns Array<Array<Int64>> (transposed) and append prints.
TEMPLATES["MATRIXTRANS"] = _tpl(
    _HELPERS,
    "func transpose(m: Array<Array<Int64>>, r: Int64, c: Int64): Array<Array<Int64>> {\n    // return the c-by-r transposed matrix\n    return m\n}",
    "main() {\n    let hdr = _ints(_rl())\n    let r = hdr[0]\n    let c = hdr[1]\n    let m = ArrayList<Array<Int64>>()\n    for (_ in 0..r) {\n        m.add(_ints(_rl()))\n    }\n    let t = transpose(m.toArray(), r, c)\n    for (row in t) {\n        let sb = StringBuilder()\n        for (i in 0..row.size) {\n            if (i > 0) { sb.append(\" \") }\n            sb.append(row[i].toString())\n        }\n        println(sb.toString())\n    }\n}")

# TWOSUM: twoSum(a, target) -> (Int64, Int64)
TEMPLATES["TWOSUM"] = _tpl(
    _HELPERS,
    "func twoSum(a: Array<Int64>, target: Int64): (Int64, Int64) {\n    // return (i, j) with i < j, or (-1, -1) if none\n    return (-1, -1)\n}",
    "main() {\n    let hdr = _ints(_rl())\n    let target = hdr[1]\n    let a = _ints(_rl())\n    let (i, j) = twoSum(a, target)\n    if (i == -1) { println(-1) } else { println(\"${i} ${j}\") }\n}")

# CLIMBSTAIRS: climbStairs(n) -> Int64
TEMPLATES["CLIMBSTAIRS"] = _tpl(
    _HELPERS,
    "func climbStairs(n: Int64): Int64 {\n    // write your code here\n    return 0\n}",
    "main() {\n    println(climbStairs(Int64.parse(_rl())))\n}")

# FIZZBUZZ: fizzBuzz(n) -> Array<String>
TEMPLATES["FIZZBUZZ"] = _tpl(
    _HELPERS,
    "func fizzBuzz(n: Int64): Array<String> {\n    // write your code here\n    return Array<String>()\n}",
    "main() {\n    let res = fizzBuzz(Int64.parse(_rl()))\n    let sb = StringBuilder()\n    for (i in 0..res.size) {\n        if (i > 0) { sb.append(\" \") }\n        sb.append(res[i])\n    }\n    println(sb.toString())\n}")

# VALIDANAG: isAnagram(s, t) -> Bool
TEMPLATES["VALIDANAG"] = _tpl(
    _HELPERS,
    "func isAnagram(s: String, t: String): Bool {\n    // write your code here\n    return false\n}",
    "main() {\n    let s = _rl()\n    let t = _rl()\n    println(if (isAnagram(s, t)) { \"Yes\" } else { \"No\" })\n}")

# STOCKPROFIT: maxProfit(prices) -> Int64
TEMPLATES["STOCKPROFIT"] = _tpl(
    _HELPERS,
    "func maxProfit(prices: Array<Int64>): Int64 {\n    // write your code here\n    return 0\n}",
    "main() {\n    let _ = _rl()\n    let prices = _ints(_rl())\n    println(maxProfit(prices))\n}")

# LONGESTSUBSTR: lengthOfLongestSubstring(s) -> Int64
TEMPLATES["LONGESTSUBSTR"] = _tpl(
    _HELPERS,
    "func lengthOfLongestSubstring(s: String): Int64 {\n    // write your code here\n    return 0\n}",
    "main() {\n    println(lengthOfLongestSubstring(_rl()))\n}")

# MERGEINTERVALS: mergeIntervals(intervals) -> Array<Array<Int64>>
TEMPLATES["MERGEINTERVALS"] = _tpl(
    _HELPERS,
    "func mergeIntervals(intervals: Array<Array<Int64>>): Array<Array<Int64>> {\n    // return merged intervals sorted by start time\n    return intervals\n}",
    "main() {\n    let n = Int64.parse(_rl())\n    let list = ArrayList<Array<Int64>>()\n    for (_ in 0..n) { list.add(_ints(_rl())) }\n    let res = mergeIntervals(list.toArray())\n    for (it in res) { println(\"${it[0]} ${it[1]}\") }\n}")

# ROTIMG: rotate(matrix, n) -> Array<Array<Int64>>
TEMPLATES["ROTIMG"] = _tpl(
    _HELPERS,
    "func rotate(matrix: Array<Array<Int64>>, n: Int64): Array<Array<Int64>> {\n    // rotate 90 degrees clockwise\n    return matrix\n}",
    "main() {\n    let n = Int64.parse(_rl())\n    let list = ArrayList<Array<Int64>>()\n    for (_ in 0..n) { list.add(_ints(_rl())) }\n    let res = rotate(list.toArray(), n)\n    for (row in res) {\n        let sb = StringBuilder()\n        for (i in 0..row.size) {\n            if (i > 0) { sb.append(\" \") }\n            sb.append(row[i].toString())\n        }\n        println(sb.toString())\n    }\n}")

# TRAPPINGRAIN: trap(height) -> Int64
TEMPLATES["TRAPPINGRAIN"] = _tpl(
    _HELPERS,
    "func trap(height: Array<Int64>): Int64 {\n    // write your code here\n    return 0\n}",
    "main() {\n    let _ = _rl()\n    let height = _ints(_rl())\n    println(trap(height))\n}")

# LIS: lengthOfLIS(nums) -> Int64
TEMPLATES["LIS"] = _tpl(
    _HELPERS,
    "func lengthOfLIS(nums: Array<Int64>): Int64 {\n    // write your code here\n    return 0\n}",
    "main() {\n    let _ = _rl()\n    let nums = _ints(_rl())\n    println(lengthOfLIS(nums))\n}")

