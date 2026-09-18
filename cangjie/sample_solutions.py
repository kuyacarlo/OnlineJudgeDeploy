"""Multi-language sample solutions (Cangjie, Python3, C, C++) for all 30 problems."""

SAMPLE_SOLUTIONS = {
    "HELLO": {
        "Cangjie": """main() {
    println("Hello, World!")
}""",
        "Python3": """print("Hello, World!")""",
        "C": """#include <stdio.h>

int main() {
    printf("Hello, World!\\n");
    return 0;
}""",
        "C++": """#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}""",
    },
    "SUMN": {
        "Cangjie": """import std.env.*
import std.convert.*

main() {
    let n = Int64.parse(getStdIn().readln().getOrThrow().trimAscii())
    println(n * (n + 1) / 2)
}""",
        "Python3": """import sys
n = int(sys.stdin.read().strip())
print(n * (n + 1) // 2)""",
        "C": """#include <stdio.h>

int main() {
    long long n;
    if (scanf("%lld", &n) == 1) {
        printf("%lld\\n", n * (n + 1) / 2);
    }
    return 0;
}""",
        "C++": """#include <iostream>

int main() {
    long long n;
    if (std::cin >> n) {
        std::cout << n * (n + 1) / 2 << std::endl;
    }
    return 0;
}""",
    },
    "APLUSB": {
        "Cangjie": """import std.env.*
import std.convert.*

main() {
    let p = getStdIn().readln().getOrThrow().trimAscii().split(" ")
    println(Int64.parse(p[0]) + Int64.parse(p[1]))
}""",
        "Python3": """import sys
a, b = map(int, sys.stdin.readline().split())
print(a + b)""",
        "C": """#include <stdio.h>

int main() {
    long long a, b;
    if (scanf("%lld %lld", &a, &b) == 2) {
        printf("%lld\\n", a + b);
    }
    return 0;
}""",
        "C++": """#include <iostream>

int main() {
    long long a, b;
    if (std::cin >> a >> b) {
        std::cout << a + b << std::endl;
    }
    return 0;
}""",
    },
    "MAXOF3": {
        "Cangjie": """import std.env.*
import std.convert.*

main() {
    let p = getStdIn().readln().getOrThrow().trimAscii().split(" ")
    var m = Int64.parse(p[0])
    let b = Int64.parse(p[1])
    let c = Int64.parse(p[2])
    if (b > m) { m = b }
    if (c > m) { m = c }
    println(m)
}""",
        "Python3": """import sys
nums = list(map(int, sys.stdin.readline().split()))
print(max(nums))""",
        "C": """#include <stdio.h>

int main() {
    long long a, b, c;
    if (scanf("%lld %lld %lld", &a, &b, &c) == 3) {
        long long m = a;
        if (b > m) m = b;
        if (c > m) m = c;
        printf("%lld\\n", m);
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <algorithm>

int main() {
    long long a, b, c;
    if (std::cin >> a >> b >> c) {
        std::cout << std::max({a, b, c}) << std::endl;
    }
    return 0;
}""",
    },
    "STRREV": {
        "Cangjie": """import std.env.*

main() {
    let s = getStdIn().readln().getOrThrow().trimAscii()
    let bytes = s.toArray()
    let sb = StringBuilder()
    var i = bytes.size - 1
    while (i >= 0) {
        sb.append(String.fromUtf8(bytes[i..i+1]))
        i--
    }
    println(sb.toString())
}""",
        "Python3": """import sys
s = sys.stdin.readline().strip()
print(s[::-1])""",
        "C": """#include <stdio.h>
#include <string.h>

int main() {
    char s[1024];
    if (scanf("%1023s", s) == 1) {
        int len = strlen(s);
        for (int i = len - 1; i >= 0; i--) {
            putchar(s[i]);
        }
        putchar('\\n');
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <string>
#include <algorithm>

int main() {
    std::string s;
    if (std::cin >> s) {
        std::reverse(s.begin(), s.end());
        std::cout << s << std::endl;
    }
    return 0;
}""",
    },
    "FACTORIAL": {
        "Cangjie": """import std.env.*
import std.convert.*

main() {
    let n = Int64.parse(getStdIn().readln().getOrThrow().trimAscii())
    var r: Int64 = 1
    var i: Int64 = 2
    while (i <= n) { r *= i; i++ }
    println(r)
}""",
        "Python3": """import sys, math
n = int(sys.stdin.read().strip())
print(math.factorial(n))""",
        "C": """#include <stdio.h>

int main() {
    int n;
    if (scanf("%d", &n) == 1) {
        long long r = 1;
        for (int i = 2; i <= n; i++) r *= i;
        printf("%lld\\n", r);
    }
    return 0;
}""",
        "C++": """#include <iostream>

int main() {
    int n;
    if (std::cin >> n) {
        long long r = 1;
        for (int i = 2; i <= n; i++) r *= i;
        std::cout << r << std::endl;
    }
    return 0;
}""",
    },
    "FIBONACCI": {
        "Cangjie": """import std.env.*
import std.convert.*

main() {
    let n = Int64.parse(getStdIn().readln().getOrThrow().trimAscii())
    if (n == 0) { println(0); return }
    var a: Int64 = 0
    var b: Int64 = 1
    var i: Int64 = 1
    while (i < n) {
        let t = a + b
        a = b
        b = t
        i++
    }
    println(b)
}""",
        "Python3": """import sys
n = int(sys.stdin.read().strip())
a, b = 0, 1
for _ in range(n):
    a, b = b, a + b
print(a)""",
        "C": """#include <stdio.h>

int main() {
    int n;
    if (scanf("%d", &n) == 1) {
        long long a = 0, b = 1;
        for (int i = 0; i < n; i++) {
            long long t = a + b;
            a = b;
            b = t;
        }
        printf("%lld\\n", a);
    }
    return 0;
}""",
        "C++": """#include <iostream>

int main() {
    int n;
    if (std::cin >> n) {
        long long a = 0, b = 1;
        for (int i = 0; i < n; i++) {
            long long t = a + b;
            a = b;
            b = t;
        }
        std::cout << a << std::endl;
    }
    return 0;
}""",
    },
    "GCDLCM": {
        "Cangjie": """import std.env.*
import std.convert.*

func gcd(a: Int64, b: Int64): Int64 {
    var x = a
    var y = b
    while (y != 0) {
        let t = x % y
        x = y
        y = t
    }
    return x
}

main() {
    let p = getStdIn().readln().getOrThrow().trimAscii().split(" ")
    let a = Int64.parse(p[0])
    let b = Int64.parse(p[1])
    let g = gcd(a, b)
    let l = a / g * b
    println("${g} ${l}")
}""",
        "Python3": """import sys, math
a, b = map(int, sys.stdin.readline().split())
g = math.gcd(a, b)
l = a * b // g
print(f"{g} {l}")""",
        "C": """#include <stdio.h>

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int main() {
    long long a, b;
    if (scanf("%lld %lld", &a, &b) == 2) {
        long long g = gcd(a, b);
        long long l = a / g * b;
        printf("%lld %lld\\n", g, l);
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <numeric>

int main() {
    long long a, b;
    if (std::cin >> a >> b) {
        long long g = std::gcd(a, b);
        long long l = a / g * b;
        std::cout << g << " " << l << std::endl;
    }
    return 0;
}""",
    },
    "PRIMETEST": {
        "Cangjie": """import std.env.*
import std.convert.*

main() {
    let n = Int64.parse(getStdIn().readln().getOrThrow().trimAscii())
    if (n < 2) { println("No"); return }
    var i: Int64 = 2
    var prime = true
    while (i * i <= n) {
        if (n % i == 0) { prime = false; break }
        i++
    }
    println(if (prime) { "Yes" } else { "No" })
}""",
        "Python3": """import sys
n = int(sys.stdin.read().strip())
def is_prime(x):
    if x < 2: return False
    i = 2
    while i * i <= x:
        if x % i == 0: return False
        i += 1
    return True
print("Yes" if is_prime(n) else "No")""",
        "C": """#include <stdio.h>
#include <stdbool.h>

int main() {
    long long n;
    if (scanf("%lld", &n) == 1) {
        if (n < 2) { printf("No\\n"); return 0; }
        bool prime = true;
        for (long long i = 2; i * i <= n; i++) {
            if (n % i == 0) { prime = false; break; }
        }
        printf("%s\\n", prime ? "Yes" : "No");
    }
    return 0;
}""",
        "C++": """#include <iostream>

int main() {
    long long n;
    if (std::cin >> n) {
        if (n < 2) { std::cout << "No\\n"; return 0; }
        bool prime = true;
        for (long long i = 2; i * i <= n; i++) {
            if (n % i == 0) { prime = false; break; }
        }
        std::cout << (prime ? "Yes" : "No") << std::endl;
    }
    return 0;
}""",
    },
    "ARREXTREMES": {
        "Cangjie": """import std.env.*
import std.convert.*

main() {
    let lines = getStdIn().readln().getOrThrow()
    let raw = getStdIn().readln().getOrThrow().trimAscii().split(" ")
    var s: Int64 = 0
    var mn: Int64 = Int64.parse(raw[0])
    var mx: Int64 = Int64.parse(raw[0])
    for (p in raw) {
        if (p.size > 0) {
            let v = Int64.parse(p)
            s += v
            if (v < mn) { mn = v }
            if (v > mx) { mx = v }
        }
    }
    println("${s} ${mn} ${mx}")
}""",
        "Python3": """import sys
lines = sys.stdin.read().split()
if lines:
    n = int(lines[0])
    arr = list(map(int, lines[1:1+n]))
    print(f"{sum(arr)} {min(arr)} {max(arr)}")""",
        "C": """#include <stdio.h>

int main() {
    int n;
    if (scanf("%d", &n) == 1 && n > 0) {
        long long sum = 0, mn, mx;
        for (int i = 0; i < n; i++) {
            long long x;
            scanf("%lld", &x);
            sum += x;
            if (i == 0 || x < mn) mn = x;
            if (i == 0 || x > mx) mx = x;
        }
        printf("%lld %lld %lld\\n", sum, mn, mx);
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

int main() {
    int n;
    if (std::cin >> n && n > 0) {
        std::vector<long long> a(n);
        for (int i = 0; i < n; i++) std::cin >> a[i];
        long long sum = std::accumulate(a.begin(), a.end(), 0LL);
        auto [mn, mx] = std::minmax_element(a.begin(), a.end());
        std::cout << sum << " " << *mn << " " << *mx << std::endl;
    }
    return 0;
}""",
    },
    "PALINDROME": {
        "Cangjie": """import std.env.*

main() {
    let s = getStdIn().readln().getOrThrow().trimAscii()
    let b = s.toArray()
    var i = 0
    var j = b.size - 1
    var pal = true
    while (i < j) {
        if (b[i] != b[j]) { pal = false; break }
        i++; j--
    }
    println(if (pal) { "Yes" } else { "No" })
}""",
        "Python3": """import sys
s = sys.stdin.readline().strip()
print("Yes" if s == s[::-1] else "No")""",
        "C": """#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main() {
    char s[1024];
    if (scanf("%1023s", s) == 1) {
        int i = 0, j = strlen(s) - 1;
        bool ok = true;
        while (i < j) {
            if (s[i++] != s[j--]) { ok = false; break; }
        }
        printf("%s\\n", ok ? "Yes" : "No");
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <string>
#include <algorithm>

int main() {
    std::string s;
    if (std::cin >> s) {
        std::string r = s;
        std::reverse(r.begin(), r.end());
        std::cout << (s == r ? "Yes" : "No") << std::endl;
    }
    return 0;
}""",
    },
    "SORTINTS": {
        "Cangjie": """import std.env.*
import std.convert.*
import std.collection.*

main() {
    let _n = getStdIn().readln().getOrThrow()
    let raw = getStdIn().readln().getOrThrow().trimAscii().split(" ")
    let arr = ArrayList<Int64>()
    for (p in raw) {
        if (p.size > 0) { arr.add(Int64.parse(p)) }
    }
    let n = arr.size
    var i = 0
    while (i < n) {
        var j = 0
        while (j + 1 < n - i) {
            if (arr[j] > arr[j + 1]) {
                let t = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = t
            }
            j++
        }
        i++
    }
    let sb = StringBuilder()
    for (k in 0..n) {
        if (k > 0) { sb.append(" ") }
        sb.append(arr[k].toString())
    }
    println(sb.toString())
}""",
        "Python3": """import sys
lines = sys.stdin.read().split()
if lines:
    n = int(lines[0])
    arr = sorted(map(int, lines[1:1+n]))
    print(*(arr))""",
        "C": """#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) {
    long long x = *(const long long *)a;
    long long y = *(const long long *)b;
    return (x > y) - (x < y);
}

int main() {
    int n;
    if (scanf("%d", &n) == 1 && n > 0) {
        long long *a = malloc(sizeof(long long) * n);
        for (int i = 0; i < n; i++) scanf("%lld", &a[i]);
        qsort(a, n, sizeof(long long), cmp);
        for (int i = 0; i < n; i++) {
            printf("%lld%c", a[i], i == n - 1 ? '\\n' : ' ');
        }
        free(a);
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    if (std::cin >> n && n > 0) {
        std::vector<long long> a(n);
        for (int i = 0; i < n; i++) std::cin >> a[i];
        std::sort(a.begin(), a.end());
        for (int i = 0; i < n; i++) {
            std::cout << a[i] << (i == n - 1 ? "" : " ");
        }
        std::cout << std::endl;
    }
    return 0;
}""",
    },
    "VOWELCOUNT": {
        "Cangjie": """import std.env.*

main() {
    let s = getStdIn().readln().getOrThrow().trimAscii()
    let bytes = s.toArray()
    var v = 0
    var c = 0
    for (b in bytes) {
        if (b == 97 || b == 101 || b == 105 || b == 111 || b == 117) {
            v++
        } else {
            c++
        }
    }
    println("${v} ${c}")
}""",
        "Python3": """import sys
s = sys.stdin.readline().strip()
v = sum(ch in 'aeiou' for ch in s)
print(f"{v} {len(s) - v}")""",
        "C": """#include <stdio.h>
#include <string.h>

int main() {
    char s[1024];
    if (scanf("%1023s", s) == 1) {
        int v = 0, c = 0;
        for (int i = 0; s[i]; i++) {
            char ch = s[i];
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') v++;
            else c++;
        }
        printf("%d %d\\n", v, c);
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <string>

int main() {
    std::string s;
    if (std::cin >> s) {
        int v = 0, c = 0;
        for (char ch : s) {
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') v++;
            else c++;
        }
        std::cout << v << " " << c << std::endl;
    }
    return 0;
}""",
    },
    "BINSEARCH": {
        "Cangjie": """import std.env.*
import std.convert.*
import std.collection.*

main() {
    let l1 = getStdIn().readln().getOrThrow().trimAscii().split(" ")
    let n = Int64.parse(l1[0])
    let target = Int64.parse(l1[1])
    let l2 = getStdIn().readln().getOrThrow().trimAscii().split(" ")
    var lo: Int64 = 0
    var hi: Int64 = n - 1
    var ans: Int64 = -1
    while (lo <= hi) {
        let mid = lo + (hi - lo) / 2
        let v = Int64.parse(l2[mid])
        if (v == target) { ans = mid; break }
        else if (v < target) { lo = mid + 1 }
        else { hi = mid - 1 }
    }
    println(ans)
}""",
        "Python3": """import sys
lines = sys.stdin.read().split()
if lines:
    n, target = int(lines[0]), int(lines[1])
    arr = list(map(int, lines[2:2+n]))
    try:
        print(arr.index(target))
    except ValueError:
        print(-1)""",
        "C": """#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    long long target;
    if (scanf("%d %lld", &n, &target) == 2) {
        long long *a = malloc(sizeof(long long) * n);
        for (int i = 0; i < n; i++) scanf("%lld", &a[i]);
        int lo = 0, hi = n - 1, ans = -1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (a[mid] == target) { ans = mid; break; }
            else if (a[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        printf("%d\\n", ans);
        free(a);
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    long long target;
    if (std::cin >> n >> target) {
        std::vector<long long> a(n);
        for (int i = 0; i < n; i++) std::cin >> a[i];
        auto it = std::lower_bound(a.begin(), a.end(), target);
        if (it != a.end() && *it == target) {
            std::cout << std::distance(a.begin(), it) << std::endl;
        } else {
            std::cout << -1 << std::endl;
        }
    }
    return 0;
}""",
    },
    "MATRIXTRANS": {
        "Cangjie": """import std.env.*
import std.convert.*
import std.collection.*

main() {
    let p = getStdIn().readln().getOrThrow().trimAscii().split(" ")
    let r = Int64.parse(p[0])
    let c = Int64.parse(p[1])
    let m = Array<Array<Int64>>(r, {_ => Array<Int64>(c, {_ => 0})})
    var i = 0
    while (i < r) {
        let row = getStdIn().readln().getOrThrow().trimAscii().split(" ")
        var j = 0
        for (x in row) {
            if (x.size > 0 && j < c) {
                m[i][j] = Int64.parse(x)
                j++
            }
        }
        i++
    }
    var j = 0
    while (j < c) {
        let sb = StringBuilder()
        var k = 0
        while (k < r) {
            if (k > 0) { sb.append(" ") }
            sb.append(m[k][j].toString())
            k++
        }
        println(sb.toString())
        j++
    }
}""",
        "Python3": """import sys
lines = sys.stdin.read().split()
if lines:
    r, c = int(lines[0]), int(lines[1])
    vals = list(map(int, lines[2:2+r*c]))
    matrix = [vals[i*c:(i+1)*c] for i in range(r)]
    for j in range(c):
        print(*(matrix[i][j] for i in range(r)))""",
        "C": """#include <stdio.h>

int main() {
    int r, c;
    if (scanf("%d %d", &r, &c) == 2) {
        long long m[105][105];
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) scanf("%lld", &m[i][j]);
        }
        for (int j = 0; j < c; j++) {
            for (int i = 0; i < r; i++) {
                printf("%lld%c", m[i][j], i == r - 1 ? '\\n' : ' ');
            }
        }
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <vector>

int main() {
    int r, c;
    if (std::cin >> r >> c) {
        std::vector<std::vector<long long>> m(r, std::vector<long long>(c));
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) std::cin >> m[i][j];
        }
        for (int j = 0; j < c; j++) {
            for (int i = 0; i < r; i++) {
                std::cout << m[i][j] << (i == r - 1 ? "" : " ");
            }
            std::cout << std::endl;
        }
    }
    return 0;
}""",
    },
    "PARENMATCH": {
        "Cangjie": """import std.env.*
import std.collection.*

main() {
    let s = getStdIn().readln().getOrThrow().trimAscii()
    let bytes = s.toArray()
    let st = ArrayList<UInt8>()
    var ok = true
    for (b in bytes) {
        if (b == 40 || b == 91 || b == 123) { // ( [ {
            st.add(b)
        } else {
            if (st.size == 0) { ok = false; break }
            let top = st[st.size - 1]
            st.remove(st.size - 1)
            if (b == 41 && top != 40) { ok = false; break }
            if (b == 93 && top != 91) { ok = false; break }
            if (b == 125 && top != 123) { ok = false; break }
        }
    }
    if (st.size != 0) { ok = false }
    println(if (ok) { "Valid" } else { "Invalid" })
}""",
        "Python3": """import sys
s = sys.stdin.readline().strip()
st = []
pairs = {')': '(', ']': '[', '}': '{'}
ok = True
for ch in s:
    if ch in "([{":
        st.append(ch)
    elif ch in pairs:
        if not st or st.pop() != pairs[ch]:
            ok = False
            break
if st: ok = False
print("Valid" if ok else "Invalid")""",
        "C": """#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main() {
    char s[10005];
    if (scanf("%10004s", s) == 1) {
        char st[10005];
        int top = 0;
        bool ok = true;
        for (int i = 0; s[i]; i++) {
            char c = s[i];
            if (c == '(' || c == '[' || c == '{') st[top++] = c;
            else {
                if (top == 0) { ok = false; break; }
                char t = st[--top];
                if (c == ')' && t != '(') { ok = false; break; }
                if (c == ']' && t != '[') { ok = false; break; }
                if (c == '}' && t != '{') { ok = false; break; }
            }
        }
        if (top != 0) ok = false;
        printf("%s\\n", ok ? "Valid" : "Invalid");
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <string>
#include <stack>

int main() {
    std::string s;
    if (std::cin >> s) {
        std::stack<char> st;
        bool ok = true;
        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') st.push(c);
            else {
                if (st.empty()) { ok = false; break; }
                char t = st.top(); st.pop();
                if (c == ')' && t != '(') { ok = false; break; }
                if (c == ']' && t != '[') { ok = false; break; }
                if (c == '}' && t != '{') { ok = false; break; }
            }
        }
        if (!st.empty()) ok = false;
        std::cout << (ok ? "Valid" : "Invalid") << std::endl;
    }
    return 0;
}""",
    },
    "MAXSUBARR": {
        "Cangjie": """import std.env.*
import std.convert.*

main() {
    let _n = getStdIn().readln().getOrThrow()
    let raw = getStdIn().readln().getOrThrow().trimAscii().split(" ")
    var best: Int64 = Int64.parse(raw[0])
    var cur: Int64 = best
    var first = true
    for (p in raw) {
        if (p.size > 0) {
            let x = Int64.parse(p)
            if (first) {
                first = false
                cur = x; best = x
            } else {
                cur = if (x > cur + x) { x } else { cur + x }
                if (cur > best) { best = cur }
            }
        }
    }
    println(best)
}""",
        "Python3": """import sys
lines = sys.stdin.read().split()
if lines:
    n = int(lines[0])
    arr = list(map(int, lines[1:1+n]))
    best = cur = arr[0]
    for x in arr[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    print(best)""",
        "C": """#include <stdio.h>

int main() {
    int n;
    if (scanf("%d", &n) == 1 && n > 0) {
        long long cur, best;
        for (int i = 0; i < n; i++) {
            long long x;
            scanf("%lld", &x);
            if (i == 0) { cur = best = x; }
            else {
                cur = (x > cur + x) ? x : cur + x;
                if (cur > best) best = cur;
            }
        }
        printf("%lld\\n", best);
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    if (std::cin >> n && n > 0) {
        long long x;
        std::cin >> x;
        long long cur = x, best = x;
        for (int i = 1; i < n; i++) {
            std::cin >> x;
            cur = std::max(x, cur + x);
            best = std::max(best, cur);
        }
        std::cout << best << std::endl;
    }
    return 0;
}""",
    },
    "COINCHANGE": {
        "Cangjie": """import std.env.*
import std.convert.*
import std.collection.*

main() {
    let l1 = getStdIn().readln().getOrThrow().trimAscii().split(" ")
    let n = Int64.parse(l1[0])
    let m = Int64.parse(l1[1])
    let l2 = getStdIn().readln().getOrThrow().trimAscii().split(" ")
    let coins = ArrayList<Int64>()
    for (p in l2) {
        if (p.size > 0) { coins.add(Int64.parse(p)) }
    }
    let INF: Int64 = 1000000000
    let dp = Array<Int64>(m + 1, {_ => INF})
    dp[0] = 0
    var a = 1
    while (a <= m) {
        for (c in coins) {
            if (c <= a && dp[a - c] + 1 < dp[a]) {
                dp[a] = dp[a - c] + 1
            }
        }
        a++
    }
    println(if (dp[m] >= INF) { -1 } else { dp[m] })
}""",
        "Python3": """import sys
lines = sys.stdin.read().split()
if lines:
    n, m = int(lines[0]), int(lines[1])
    coins = list(map(int, lines[2:2+n]))
    INF = float('inf')
    dp = [0] + [INF] * m
    for a in range(1, m + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    print(dp[m] if dp[m] != INF else -1)""",
        "C": """#include <stdio.h>
#include <stdlib.h>

#define INF 1000000000

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) == 2) {
        int *coins = malloc(sizeof(int) * n);
        for (int i = 0; i < n; i++) scanf("%d", &coins[i]);
        int *dp = malloc(sizeof(int) * (m + 1));
        dp[0] = 0;
        for (int i = 1; i <= m; i++) dp[i] = INF;
        for (int a = 1; a <= m; a++) {
            for (int j = 0; j < n; j++) {
                if (coins[j] <= a && dp[a - coins[j]] + 1 < dp[a]) {
                    dp[a] = dp[a - coins[j]] + 1;
                }
            }
        }
        printf("%d\\n", dp[m] >= INF ? -1 : dp[m]);
        free(coins);
        free(dp);
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n, m;
    if (std::cin >> n >> m) {
        std::vector<int> coins(n);
        for (int i = 0; i < n; i++) std::cin >> coins[i];
        const int INF = 1e9;
        std::vector<int> dp(m + 1, INF);
        dp[0] = 0;
        for (int a = 1; a <= m; a++) {
            for (int c : coins) {
                if (c <= a) dp[a] = std::min(dp[a], dp[a - c] + 1);
            }
        }
        std::cout << (dp[m] >= INF ? -1 : dp[m]) << std::endl;
    }
    return 0;
}""",
    },
    "LCS": {
        "Cangjie": """import std.env.*

main() {
    let s = getStdIn().readln().getOrThrow().trimAscii()
    let t = getStdIn().readln().getOrThrow().trimAscii()
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
    println(dp[n][m])
}""",
        "Python3": """import sys
lines = sys.stdin.read().split()
if len(lines) >= 2:
    s, t = lines[0], lines[1]
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp[n][m])""",
        "C": """#include <stdio.h>
#include <string.h>

int dp[1005][1005];

int main() {
    char s[1005], t[1005];
    if (scanf("%1004s %1004s", s, t) == 2) {
        int n = strlen(s), m = strlen(t);
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (s[i - 1] == t[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
                else dp[i][j] = (dp[i - 1][j] > dp[i][j - 1]) ? dp[i - 1][j] : dp[i][j - 1];
            }
        }
        printf("%d\\n", dp[n][m]);
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main() {
    std::string s, t;
    if (std::cin >> s >> t) {
        int n = s.size(), m = t.size();
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(m + 1, 0));
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (s[i - 1] == t[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
                else dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        std::cout << dp[n][m] << std::endl;
    }
    return 0;
}""",
    },
    "KNAPSACK01": {
        "Cangjie": """import std.env.*
import std.convert.*

main() {
    let p = getStdIn().readln().getOrThrow().trimAscii().split(" ")
    let n = Int64.parse(p[0])
    let w = Int64.parse(p[1])
    let dp = Array<Int64>(w + 1, {_ => 0})
    var i = 0
    while (i < n) {
        let it = getStdIn().readln().getOrThrow().trimAscii().split(" ")
        let wt = Int64.parse(it[0])
        let val = Int64.parse(it[1])
        var c = w
        while (c >= wt) {
            let cand = dp[c - wt] + val
            if (cand > dp[c]) { dp[c] = cand }
            c--
        }
        i++
    }
    println(dp[w])
}""",
        "Python3": """import sys
lines = sys.stdin.read().split()
if lines:
    n, w = int(lines[0]), int(lines[1])
    idx = 2
    dp = [0] * (w + 1)
    for _ in range(n):
        wt, val = int(lines[idx]), int(lines[idx + 1])
        idx += 2
        for c in range(w, wt - 1, -1):
            dp[c] = max(dp[c], dp[c - wt] + val)
    print(dp[w])""",
        "C": """#include <stdio.h>

long long dp[1005];

int main() {
    int n, w;
    if (scanf("%d %d", &n, &w) == 2) {
        for (int i = 0; i < n; i++) {
            int wt;
            long long val;
            scanf("%d %lld", &wt, &val);
            for (int c = w; c >= wt; c--) {
                if (dp[c - wt] + val > dp[c]) {
                    dp[c] = dp[c - wt] + val;
                }
            }
        }
        printf("%lld\\n", dp[w]);
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n, w;
    if (std::cin >> n >> w) {
        std::vector<long long> dp(w + 1, 0);
        for (int i = 0; i < n; i++) {
            int wt;
            long long val;
            std::cin >> wt >> val;
            for (int c = w; c >= wt; c--) {
                dp[c] = std::max(dp[c], dp[c - wt] + val);
            }
        }
        std::cout << dp[w] << std::endl;
    }
    return 0;
}""",
    },
    "TWOSUM": {
        "Cangjie": """import std.env.*
import std.convert.*
import std.collection.*

main() {
    let l1 = getStdIn().readln().getOrThrow().trimAscii().split(" ")
    let n = Int64.parse(l1[0])
    let target = Int64.parse(l1[1])
    let l2 = getStdIn().readln().getOrThrow().trimAscii().split(" ")
    let map = HashMap<Int64, Int64>()
    var found = false
    var i: Int64 = 0
    while (i < n) {
        let x = Int64.parse(l2[i])
        let complement = target - x
        if (map.contains(complement)) {
            let j = map[complement]
            println("${j} ${i}")
            found = true
            break
        }
        map[x] = i
        i++
    }
    if (!found) { println(-1) }
}""",
        "Python3": """import sys
lines = sys.stdin.read().split()
if lines:
    n, target = int(lines[0]), int(lines[1])
    arr = list(map(int, lines[2:2+n]))
    seen = {}
    for i, x in enumerate(arr):
        if target - x in seen:
            print(f"{seen[target - x]} {i}")
            break
        seen[x] = i
    else:
        print(-1)""",
        "C": """#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    long long target;
    if (scanf("%d %lld", &n, &target) == 2) {
        long long *a = malloc(sizeof(long long) * n);
        for (int i = 0; i < n; i++) scanf("%lld", &a[i]);
        int found = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (a[i] + a[j] == target) {
                    printf("%d %d\\n", i, j);
                    found = 1;
                    break;
                }
            }
            if (found) break;
        }
        if (!found) printf("-1\\n");
        free(a);
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <vector>
#include <unordered_map>

int main() {
    int n;
    long long target;
    if (std::cin >> n >> target) {
        std::vector<long long> a(n);
        std::unordered_map<long long, int> map;
        bool found = false;
        for (int i = 0; i < n; i++) {
            std::cin >> a[i];
            long long comp = target - a[i];
            if (map.count(comp)) {
                std::cout << map[comp] << " " << i << std::endl;
                found = true;
                break;
            }
            map[a[i]] = i;
        }
        if (!found) std::cout << -1 << std::endl;
    }
    return 0;
}""",
    },
    "CLIMBSTAIRS": {
        "Cangjie": """import std.env.*
import std.convert.*

main() {
    let n = Int64.parse(getStdIn().readln().getOrThrow().trimAscii())
    if (n <= 2) { println(n); return }
    var a: Int64 = 1
    var b: Int64 = 2
    var i: Int64 = 3
    while (i <= n) {
        let t = a + b
        a = b
        b = t
        i++
    }
    println(b)
}""",
        "Python3": """import sys
n = int(sys.stdin.read().strip())
if n <= 2:
    print(n)
else:
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    print(b)""",
        "C": """#include <stdio.h>

int main() {
    int n;
    if (scanf("%d", &n) == 1) {
        if (n <= 2) { printf("%d\\n", n); return 0; }
        long long a = 1, b = 2;
        for (int i = 3; i <= n; i++) {
            long long t = a + b;
            a = b;
            b = t;
        }
        printf("%lld\\n", b);
    }
    return 0;
}""",
        "C++": """#include <iostream>

int main() {
    int n;
    if (std::cin >> n) {
        if (n <= 2) { std::cout << n << std::endl; return 0; }
        long long a = 1, b = 2;
        for (int i = 3; i <= n; i++) {
            long long t = a + b;
            a = b;
            b = t;
        }
        std::cout << b << std::endl;
    }
    return 0;
}""",
    },
    "FIZZBUZZ": {
        "Cangjie": """import std.env.*
import std.convert.*

main() {
    let n = Int64.parse(getStdIn().readln().getOrThrow().trimAscii())
    let sb = StringBuilder()
    var i: Int64 = 1
    while (i <= n) {
        if (i > 1) { sb.append(" ") }
        if (i % 15 == 0) { sb.append("FizzBuzz") }
        else if (i % 3 == 0) { sb.append("Fizz") }
        else if (i % 5 == 0) { sb.append("Buzz") }
        else { sb.append(i.toString()) }
        i++
    }
    println(sb.toString())
}""",
        "Python3": """import sys
n = int(sys.stdin.read().strip())
res = []
for i in range(1, n + 1):
    if i % 15 == 0: res.append("FizzBuzz")
    elif i % 3 == 0: res.append("Fizz")
    elif i % 5 == 0: res.append("Buzz")
    else: res.append(str(i))
print(*(res))""",
        "C": """#include <stdio.h>

int main() {
    int n;
    if (scanf("%d", &n) == 1) {
        for (int i = 1; i <= n; i++) {
            if (i > 1) putchar(' ');
            if (i % 15 == 0) printf("FizzBuzz");
            else if (i % 3 == 0) printf("Fizz");
            else if (i % 5 == 0) printf("Buzz");
            else printf("%d", i);
        }
        putchar('\\n');
    }
    return 0;
}""",
        "C++": """#include <iostream>

int main() {
    int n;
    if (std::cin >> n) {
        for (int i = 1; i <= n; i++) {
            if (i > 1) std::cout << " ";
            if (i % 15 == 0) std::cout << "FizzBuzz";
            else if (i % 3 == 0) std::cout << "Fizz";
            else if (i % 5 == 0) std::cout << "Buzz";
            else std::cout << i;
        }
        std::cout << std::endl;
    }
    return 0;
}""",
    },
    "VALIDANAG": {
        "Cangjie": """import std.env.*

main() {
    let s = getStdIn().readln().getOrThrow().trimAscii()
    let t = getStdIn().readln().getOrThrow().trimAscii()
    if (s.size != t.size) { println("No"); return }
    let cnt = Array<Int64>(26, {_ => 0})
    for (b in s.toArray()) { cnt[Int64(b) - 97]++ }
    for (b in t.toArray()) { cnt[Int64(b) - 97]-- }
    var ok = true
    for (c in cnt) {
        if (c != 0) { ok = false; break }
    }
    println(if (ok) { "Yes" } else { "No" })
}""",
        "Python3": """import sys
lines = sys.stdin.read().split()
if len(lines) >= 2:
    s, t = lines[0], lines[1]
    print("Yes" if sorted(s) == sorted(t) else "No")""",
        "C": """#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main() {
    char s[100005], t[100005];
    if (scanf("%100004s %100004s", s, t) == 2) {
        if (strlen(s) != strlen(t)) { printf("No\\n"); return 0; }
        int cnt[26] = {0};
        for (int i = 0; s[i]; i++) cnt[s[i] - 'a']++;
        for (int i = 0; t[i]; i++) cnt[t[i] - 'a']--;
        bool ok = true;
        for (int i = 0; i < 26; i++) {
            if (cnt[i] != 0) { ok = false; break; }
        }
        printf("%s\\n", ok ? "Yes" : "No");
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <string>
#include <vector>

int main() {
    std::string s, t;
    if (std::cin >> s >> t) {
        if (s.size() != t.size()) { std::cout << "No\\n"; return 0; }
        std::vector<int> cnt(26, 0);
        for (char c : s) cnt[c - 'a']++;
        for (char c : t) cnt[c - 'a']--;
        bool ok = true;
        for (int c : cnt) {
            if (c != 0) { ok = false; break; }
        }
        std::cout << (ok ? "Yes" : "No") << std::endl;
    }
    return 0;
}""",
    },
    "STOCKPROFIT": {
        "Cangjie": """import std.env.*
import std.convert.*

main() {
    let _n = getStdIn().readln().getOrThrow()
    let raw = getStdIn().readln().getOrThrow().trimAscii().split(" ")
    var minPrice: Int64 = 1000000000
    var maxProfit: Int64 = 0
    for (p in raw) {
        if (p.size > 0) {
            let price = Int64.parse(p)
            if (price < minPrice) { minPrice = price }
            let profit = price - minPrice
            if (profit > maxProfit) { maxProfit = profit }
        }
    }
    println(maxProfit)
}""",
        "Python3": """import sys
lines = sys.stdin.read().split()
if lines:
    n = int(lines[0])
    prices = list(map(int, lines[1:1+n]))
    min_p = float('inf')
    max_profit = 0
    for p in prices:
        if p < min_p: min_p = p
        if p - min_p > max_profit: max_profit = p - min_p
    print(max_profit)""",
        "C": """#include <stdio.h>

int main() {
    int n;
    if (scanf("%d", &n) == 1 && n > 0) {
        long long min_p = 1e18, max_profit = 0;
        for (int i = 0; i < n; i++) {
            long long p;
            scanf("%lld", &p);
            if (p < min_p) min_p = p;
            if (p - min_p > max_profit) max_profit = p - min_p;
        }
        printf("%lld\\n", max_profit);
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    if (std::cin >> n && n > 0) {
        long long min_p = 1e18, max_profit = 0;
        for (int i = 0; i < n; i++) {
            long long p;
            std::cin >> p;
            min_p = std::min(min_p, p);
            max_profit = std::max(max_profit, p - min_p);
        }
        std::cout << max_profit << std::endl;
    }
    return 0;
}""",
    },
    "LONGESTSUBSTR": {
        "Cangjie": """import std.env.*
import std.collection.*

main() {
    let s = getStdIn().readln().getOrThrow().trimAscii()
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
    println(maxLen)
}""",
        "Python3": """import sys
s = sys.stdin.readline().strip()
last = {}
left = 0
max_len = 0
for i, ch in enumerate(s):
    if ch in last and last[ch] >= left:
        left = last[ch] + 1
    last[ch] = i
    max_len = max(max_len, i - left + 1)
print(max_len)""",
        "C": """#include <stdio.h>
#include <string.h>

int main() {
    char s[10005];
    if (scanf("%10004s", s) == 1) {
        int last[256];
        for (int i = 0; i < 256; i++) last[i] = -1;
        int left = 0, max_len = 0;
        for (int i = 0; s[i]; i++) {
            unsigned char c = (unsigned char)s[i];
            if (last[c] >= left) left = last[c] + 1;
            last[c] = i;
            int cur = i - left + 1;
            if (cur > max_len) max_len = cur;
        }
        printf("%d\\n", max_len);
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main() {
    std::string s;
    if (std::cin >> s) {
        std::vector<int> last(256, -1);
        int left = 0, max_len = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            unsigned char c = s[i];
            if (last[c] >= left) left = last[c] + 1;
            last[c] = i;
            max_len = std::max(max_len, i - left + 1);
        }
        std::cout << max_len << std::endl;
    }
    return 0;
}""",
    },
    "MERGEINTERVALS": {
        "Cangjie": """import std.env.*
import std.convert.*
import std.collection.*

class Interval {
    var start: Int64
    var end: Int64
    init(start: Int64, end: Int64) {
        this.start = start
        this.end = end
    }
}

main() {
    let n = Int64.parse(getStdIn().readln().getOrThrow().trimAscii())
    let list = ArrayList<Interval>()
    var i = 0
    while (i < n) {
        let p = getStdIn().readln().getOrThrow().trimAscii().split(" ")
        list.add(Interval(Int64.parse(p[0]), Int64.parse(p[1])))
        i++
    }
    // Bubble sort intervals by start
    var a = 0
    while (a < list.size) {
        var b = 0
        while (b + 1 < list.size - a) {
            if (list[b].start > list[b + 1].start) {
                let t = list[b]
                list[b] = list[b + 1]
                list[b + 1] = t
            }
            b++
        }
        a++
    }
    let merged = ArrayList<Interval>()
    for (it in list) {
        if (merged.size == 0 || merged[merged.size - 1].end < it.start) {
            merged.add(Interval(it.start, it.end))
        } else {
            let last = merged[merged.size - 1]
            if (it.end > last.end) { last.end = it.end }
        }
    }
    for (m in merged) {
        println("${m.start} ${m.end}")
    }
}""",
        "Python3": """import sys
lines = sys.stdin.read().split()
if lines:
    n = int(lines[0])
    intervals = []
    idx = 1
    for _ in range(n):
        intervals.append((int(lines[idx]), int(lines[idx + 1])))
        idx += 2
    intervals.sort()
    merged = []
    for s, e in intervals:
        if not merged or merged[-1][1] < s:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)
    for s, e in merged:
        print(f"{s} {e}")""",
        "C": """#include <stdio.h>
#include <stdlib.h>

typedef struct { long long s, e; } Interval;

int cmp(const void *a, const void *b) {
    const Interval *x = a, *y = b;
    if (x->s != y->s) return (x->s > y->s) - (x->s < y->s);
    return (x->e > y->e) - (x->e < y->e);
}

int main() {
    int n;
    if (scanf("%d", &n) == 1 && n > 0) {
        Interval *arr = malloc(sizeof(Interval) * n);
        for (int i = 0; i < n; i++) scanf("%lld %lld", &arr[i].s, &arr[i].e);
        qsort(arr, n, sizeof(Interval), cmp);
        Interval *merged = malloc(sizeof(Interval) * n);
        int m_len = 0;
        for (int i = 0; i < n; i++) {
            if (m_len == 0 || merged[m_len - 1].e < arr[i].s) {
                merged[m_len++] = arr[i];
            } else {
                if (arr[i].e > merged[m_len - 1].e) merged[m_len - 1].e = arr[i].e;
            }
        }
        for (int i = 0; i < m_len; i++) printf("%lld %lld\\n", merged[i].s, merged[i].e);
        free(arr);
        free(merged);
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <vector>
#include <algorithm>

struct Interval { long long s, e; };

int main() {
    int n;
    if (std::cin >> n && n > 0) {
        std::vector<Interval> a(n);
        for (int i = 0; i < n; i++) std::cin >> a[i].s >> a[i].e;
        std::sort(a.begin(), a.end(), [](const Interval &x, const Interval &y) {
            return x.s < y.s;
        });
        std::vector<Interval> merged;
        for (const auto &it : a) {
            if (merged.empty() || merged.back().e < it.s) merged.push_back(it);
            else merged.back().e = std::max(merged.back().e, it.e);
        }
        for (const auto &it : merged) std::cout << it.s << " " << it.e << std::endl;
    }
    return 0;
}""",
    },
    "ROTIMG": {
        "Cangjie": """import std.env.*
import std.convert.*

main() {
    let n = Int64.parse(getStdIn().readln().getOrThrow().trimAscii())
    let m = Array<Array<Int64>>(n, {_ => Array<Int64>(n, {_ => 0})})
    var i = 0
    while (i < n) {
        let row = getStdIn().readln().getOrThrow().trimAscii().split(" ")
        var j = 0
        for (x in row) {
            if (x.size > 0 && j < n) {
                m[i][j] = Int64.parse(x)
                j++
            }
        }
        i++
    }
    // Rotate 90 deg clockwise: new[j][n-1-i] = old[i][j]
    var r = 0
    while (r < n) {
        let sb = StringBuilder()
        var c = 0
        while (c < n) {
            if (c > 0) { sb.append(" ") }
            sb.append(m[n - 1 - c][r].toString())
            c++
        }
        println(sb.toString())
        r++
    }
}""",
        "Python3": """import sys
lines = sys.stdin.read().split()
if lines:
    n = int(lines[0])
    vals = list(map(int, lines[1:1+n*n]))
    matrix = [vals[i*n:(i+1)*n] for i in range(n)]
    # 90 deg clockwise rotation
    rotated = [[matrix[n - 1 - j][i] for j in range(n)] for i in range(n)]
    for row in rotated:
        print(*(row))""",
        "C": """#include <stdio.h>

int main() {
    int n;
    if (scanf("%d", &n) == 1) {
        long long m[105][105];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) scanf("%lld", &m[i][j]);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                printf("%lld%c", m[n - 1 - j][i], j == n - 1 ? '\\n' : ' ');
            }
        }
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <vector>

int main() {
    int n;
    if (std::cin >> n) {
        std::vector<std::vector<long long>> m(n, std::vector<long long>(n));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) std::cin >> m[i][j];
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                std::cout << m[n - 1 - j][i] << (j == n - 1 ? "" : " ");
            }
            std::cout << std::endl;
        }
    }
    return 0;
}""",
    },
    "TRAPPINGRAIN": {
        "Cangjie": """import std.env.*
import std.convert.*
import std.collection.*

main() {
    let _n = getStdIn().readln().getOrThrow()
    let raw = getStdIn().readln().getOrThrow().trimAscii().split(" ")
    let h = ArrayList<Int64>()
    for (p in raw) {
        if (p.size > 0) { h.add(Int64.parse(p)) }
    }
    let n = h.size
    if (n < 3) { println(0); return }
    var left: Int64 = 0
    var right: Int64 = n - 1
    var leftMax: Int64 = 0
    var rightMax: Int64 = 0
    var water: Int64 = 0
    while (left < right) {
        if (h[left] < h[right]) {
            if (h[left] >= leftMax) { leftMax = h[left] }
            else { water += leftMax - h[left] }
            left++
        } else {
            if (h[right] >= rightMax) { rightMax = h[right] }
            else { water += rightMax - h[right] }
            right--
        }
    }
    println(water)
}""",
        "Python3": """import sys
lines = sys.stdin.read().split()
if lines:
    n = int(lines[0])
    h = list(map(int, lines[1:1+n]))
    left, right = 0, n - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if h[left] < h[right]:
            if h[left] >= left_max: left_max = h[left]
            else: water += left_max - h[left]
            left += 1
        else:
            if h[right] >= right_max: right_max = h[right]
            else: water += right_max - h[right]
            right -= 1
    print(water)""",
        "C": """#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    if (scanf("%d", &n) == 1 && n > 0) {
        long long *h = malloc(sizeof(long long) * n);
        for (int i = 0; i < n; i++) scanf("%lld", &h[i]);
        int left = 0, right = n - 1;
        long long left_max = 0, right_max = 0, water = 0;
        while (left < right) {
            if (h[left] < h[right]) {
                if (h[left] >= left_max) left_max = h[left];
                else water += left_max - h[left];
                left++;
            } else {
                if (h[right] >= right_max) right_max = h[right];
                else water += right_max - h[right];
                right--;
            }
        }
        printf("%lld\\n", water);
        free(h);
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    if (std::cin >> n && n > 0) {
        std::vector<long long> h(n);
        for (int i = 0; i < n; i++) std::cin >> h[i];
        int left = 0, right = n - 1;
        long long left_max = 0, right_max = 0, water = 0;
        while (left < right) {
            if (h[left] < h[right]) {
                if (h[left] >= left_max) left_max = h[left];
                else water += left_max - h[left];
                left++;
            } else {
                if (h[right] >= right_max) right_max = h[right];
                else water += right_max - h[right];
                right--;
            }
        }
        std::cout << water << std::endl;
    }
    return 0;
}""",
    },
    "LIS": {
        "Cangjie": """import std.env.*
import std.convert.*
import std.collection.*

main() {
    let _n = getStdIn().readln().getOrThrow()
    let raw = getStdIn().readln().getOrThrow().trimAscii().split(" ")
    let tails = ArrayList<Int64>()
    for (p in raw) {
        if (p.size > 0) {
            let x = Int64.parse(p)
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
    }
    println(tails.size)
}""",
        "Python3": """import sys, bisect
lines = sys.stdin.read().split()
if lines:
    n = int(lines[0])
    arr = list(map(int, lines[1:1+n]))
    tails = []
    for x in arr:
        idx = bisect.bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x
    print(len(tails))""",
        "C": """#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    if (scanf("%d", &n) == 1 && n > 0) {
        long long *tails = malloc(sizeof(long long) * n);
        int len = 0;
        for (int i = 0; i < n; i++) {
            long long x;
            scanf("%lld", &x);
            int lo = 0, hi = len;
            while (lo < hi) {
                int mid = lo + (hi - lo) / 2;
                if (tails[mid] < x) lo = mid + 1;
                else hi = mid;
            }
            tails[lo] = x;
            if (lo == len) len++;
        }
        printf("%d\\n", len);
        free(tails);
    }
    return 0;
}""",
        "C++": """#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    if (std::cin >> n && n > 0) {
        std::vector<long long> tails;
        for (int i = 0; i < n; i++) {
            long long x;
            std::cin >> x;
            auto it = std::lower_bound(tails.begin(), tails.end(), x);
            if (it == tails.end()) tails.push_back(x);
            else *it = x;
        }
        std::cout << tails.size() << std::endl;
    }
    return 0;
}""",
    },
}
