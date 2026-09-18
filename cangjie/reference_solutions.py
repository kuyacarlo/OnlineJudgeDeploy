"""Reference Cangjie function-body solutions, keyed by _id. Used only to verify
the templates compile and produce correct answers (prepend+this+append)."""

REFS = {}

REFS["HELLO"] = """func solve(): String {
    return "Hello, World!"
}"""

REFS["SUMN"] = """func sumToN(n: Int64): Int64 {
    return n * (n + 1) / 2
}"""

REFS["APLUSB"] = """func add(a: Int64, b: Int64): Int64 {
    return a + b
}"""

REFS["MAXOF3"] = """func maxOf3(a: Int64, b: Int64, c: Int64): Int64 {
    var m = a
    if (b > m) { m = b }
    if (c > m) { m = c }
    return m
}"""

REFS["STRREV"] = """func reverseString(s: String): String {
    let bytes = s.toArray()
    let sb = StringBuilder()
    var i = bytes.size - 1
    while (i >= 0) {
        sb.append(String.fromUtf8(bytes[i..i+1]))
        i--
    }
    return sb.toString()
}"""

REFS["FACTORIAL"] = """func factorial(n: Int64): Int64 {
    var r = 1
    var i = 2
    while (i <= n) { r *= i; i++ }
    return r
}"""

REFS["FIBONACCI"] = """func fib(n: Int64): Int64 {
    if (n == 0) { return 0 }
    var a = 0
    var b = 1
    var i = 1
    while (i < n) { let t = a + b; a = b; b = t; i++ }
    return b
}"""

REFS["GCDLCM"] = """func gcdLcm(a: Int64, b: Int64): (Int64, Int64) {
    var x = a
    var y = b
    while (y != 0) { let t = x % y; x = y; y = t }
    return (x, a / x * b)
}"""

REFS["PRIMETEST"] = """func isPrime(n: Int64): Bool {
    if (n < 2) { return false }
    var i = 2
    while (i * i <= n) {
        if (n % i == 0) { return false }
        i++
    }
    return true
}"""

REFS["ARREXTREMES"] = """func analyze(a: Array<Int64>): (Int64, Int64, Int64) {
    var s = 0
    var mn = a[0]
    var mx = a[0]
    for (x in a) {
        s += x
        if (x < mn) { mn = x }
        if (x > mx) { mx = x }
    }
    return (s, mn, mx)
}"""

REFS["PALINDROME"] = """func isPalindrome(s: String): Bool {
    let b = s.toArray()
    var i = 0
    var j = b.size - 1
    while (i < j) {
        if (b[i] != b[j]) { return false }
        i++
        j--
    }
    return true
}"""

REFS["SORTINTS"] = """func sortInts(a: Array<Int64>): Array<Int64> {
    let n = a.size
    var i = 0
    while (i < n) {
        var j = 0
        while (j < n - 1 - i) {
            if (a[j] > a[j+1]) { let t = a[j]; a[j] = a[j+1]; a[j+1] = t }
            j++
        }
        i++
    }
    return a
}"""

REFS["VOWELCOUNT"] = """func countVC(s: String): (Int64, Int64) {
    var v = 0
    var c = 0
    for (ch in s.toArray()) {
        if (ch == b'a' || ch == b'e' || ch == b'i' || ch == b'o' || ch == b'u') {
            v++
        } else {
            c++
        }
    }
    return (v, c)
}"""

REFS["MAXSUBARR"] = """func maxSubarray(a: Array<Int64>): Int64 {
    var best = a[0]
    var cur = a[0]
    var i = 1
    while (i < a.size) {
        let x = a[i]
        cur = if (cur + x > x) { cur + x } else { x }
        if (cur > best) { best = cur }
        i++
    }
    return best
}"""

REFS["BINSEARCH"] = """func search(a: Array<Int64>, k: Int64): Int64 {
    var lo = 0
    var hi = a.size - 1
    while (lo <= hi) {
        let mid = (lo + hi) / 2
        if (a[mid] == k) { return mid }
        if (a[mid] < k) { lo = mid + 1 } else { hi = mid - 1 }
    }
    return -1
}"""

REFS["COINCHANGE"] = """func minCoins(coins: Array<Int64>, m: Int64): Int64 {
    let INF = 1000000000
    let dp = Array<Int64>(m + 1, {_ => INF})
    dp[0] = 0
    var a = 1
    while (a <= m) {
        for (c in coins) {
            if (c <= a && dp[a - c] + 1 < dp[a]) { dp[a] = dp[a - c] + 1 }
        }
        a++
    }
    if (dp[m] >= INF) { return -1 }
    return dp[m]
}"""

REFS["LCS"] = """func lcs(s: String, t: String): Int64 {
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
}"""

REFS["KNAPSACK01"] = """func knapsack(weights: Array<Int64>, values: Array<Int64>, W: Int64): Int64 {
    let dp = Array<Int64>(W + 1, {_ => 0})
    var idx = 0
    while (idx < weights.size) {
        let wt = weights[idx]
        let vl = values[idx]
        var c = W
        while (c >= wt) {
            if (dp[c - wt] + vl > dp[c]) { dp[c] = dp[c - wt] + vl }
            c--
        }
        idx++
    }
    var best = 0
    for (x in dp) { if (x > best) { best = x } }
    return best
}"""

REFS["PARENMATCH"] = """func isValid(s: String): Bool {
    let st = ArrayList<UInt8>()
    for (ch in s.toArray()) {
        if (ch == b'(' || ch == b'[' || ch == b'{') {
            st.add(ch)
        } else {
            if (st.size == 0) { return false }
            let top = st[st.size - 1]
            let ok = (ch == b')' && top == b'(') || (ch == b']' && top == b'[') || (ch == b'}' && top == b'{')
            if (!ok) { return false }
            st.remove(at: st.size - 1)
        }
    }
    return st.size == 0
}"""

REFS["MATRIXTRANS"] = """func transpose(m: Array<Array<Int64>>, r: Int64, c: Int64): Array<Array<Int64>> {
    let t = Array<Array<Int64>>(c, {_ => Array<Int64>(r, {_ => 0})})
    var i = 0
    while (i < r) {
        var j = 0
        while (j < c) {
            t[j][i] = m[i][j]
            j++
        }
        i++
    }
    return t
}"""

REFS["TWOSUM"] = """func twoSum(a: Array<Int64>, target: Int64): (Int64, Int64) {
    let map = HashMap<Int64, Int64>()
    var i: Int64 = 0
    while (i < a.size) {
        let comp = target - a[i]
        if (map.contains(comp)) {
            return (map[comp], i)
        }
        map[a[i]] = i
        i++
    }
    return (-1, -1)
}"""

REFS["CLIMBSTAIRS"] = """func climbStairs(n: Int64): Int64 {
    if (n <= 2) { return n }
    var a: Int64 = 1
    var b: Int64 = 2
    var i: Int64 = 3
    while (i <= n) {
        let t = a + b
        a = b
        b = t
        i++
    }
    return b
}"""

REFS["FIZZBUZZ"] = """func fizzBuzz(n: Int64): Array<String> {
    let list = ArrayList<String>()
    var i: Int64 = 1
    while (i <= n) {
        if (i % 15 == 0) { list.add("FizzBuzz") }
        else if (i % 3 == 0) { list.add("Fizz") }
        else if (i % 5 == 0) { list.add("Buzz") }
        else { list.add(i.toString()) }
        i++
    }
    return list.toArray()
}"""

REFS["VALIDANAG"] = """func isAnagram(s: String, t: String): Bool {
    if (s.size != t.size) { return false }
    let cnt = Array<Int64>(26, {_ => 0})
    for (b in s.toArray()) { cnt[Int64(b) - 97]++ }
    for (b in t.toArray()) { cnt[Int64(b) - 97]-- }
    for (c in cnt) {
        if (c != 0) { return false }
    }
    return true
}"""

REFS["STOCKPROFIT"] = """func maxProfit(prices: Array<Int64>): Int64 {
    var minP: Int64 = 1000000000
    var maxP: Int64 = 0
    for (p in prices) {
        if (p < minP) { minP = p }
        let diff = p - minP
        if (diff > maxP) { maxP = diff }
    }
    return maxP
}"""

REFS["LONGESTSUBSTR"] = """func lengthOfLongestSubstring(s: String): Int64 {
    let bytes = s.toArray()
    let last = HashMap<UInt8, Int64>()
    var maxLen: Int64 = 0
    var left: Int64 = 0
    var i: Int64 = 0
    while (i < bytes.size) {
        let b = bytes[i]
        if (last.contains(b)) {
            let prev = last[b]
            if (prev >= left) { left = prev + 1 }
        }
        last[b] = i
        let cur = i - left + 1
        if (cur > maxLen) { maxLen = cur }
        i++
    }
    return maxLen
}"""

REFS["MERGEINTERVALS"] = """func mergeIntervals(intervals: Array<Array<Int64>>): Array<Array<Int64>> {
    let list = ArrayList<Array<Int64>>()
    for (it in intervals) { list.add(it) }
    var a = 0
    while (a < list.size) {
        var b = 0
        while (b + 1 < list.size - a) {
            if (list[b][0] > list[b + 1][0]) {
                let t = list[b]
                list[b] = list[b + 1]
                list[b + 1] = t
            }
            b++
        }
        a++
    }
    let merged = ArrayList<Array<Int64>>()
    for (it in list) {
        if (merged.size == 0 || merged[merged.size - 1][1] < it[0]) {
            merged.add(it)
        } else {
            let last = merged[merged.size - 1]
            if (it[1] > last[1]) { last[1] = it[1] }
        }
    }
    return merged.toArray()
}"""

REFS["ROTIMG"] = """func rotate(matrix: Array<Array<Int64>>, n: Int64): Array<Array<Int64>> {
    let res = Array<Array<Int64>>(n, {_ => Array<Int64>(n, {_ => 0})})
    var r: Int64 = 0
    while (r < n) {
        var c: Int64 = 0
        while (c < n) {
            res[r][c] = matrix[n - 1 - c][r]
            c++
        }
        r++
    }
    return res
}"""

REFS["TRAPPINGRAIN"] = """func trap(height: Array<Int64>): Int64 {
    let n = height.size
    if (n < 3) { return 0 }
    var left: Int64 = 0
    var right: Int64 = n - 1
    var leftMax: Int64 = 0
    var rightMax: Int64 = 0
    var water: Int64 = 0
    while (left < right) {
        if (height[left] < height[right]) {
            if (height[left] >= leftMax) { leftMax = height[left] }
            else { water += leftMax - height[left] }
            left++
        } else {
            if (height[right] >= rightMax) { rightMax = height[right] }
            else { water += rightMax - height[right] }
            right--
        }
    }
    return water
}"""

REFS["LIS"] = """func lengthOfLIS(nums: Array<Int64>): Int64 {
    let tails = ArrayList<Int64>()
    for (x in nums) {
        var lo = 0
        var hi = tails.size
        while (lo < hi) {
            let mid = lo + (hi - lo) / 2
            if (tails[mid] < x) { lo = mid + 1 }
            else { hi = mid }
        }
        if (lo == tails.size) { tails.add(x) }
        else { tails[lo] = x }
    }
    return Int64(tails.size)
}"""

