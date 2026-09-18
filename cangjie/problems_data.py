"""Full catalog of 30 curated algorithm problems with rigorous test cases."""

PROBLEMS = [
    {
        "_id": "HELLO",
        "title": "Hello, World!",
        "description": "Output the classic greeting string `Hello, World!`.",
        "input_description": "There is no input for this problem.",
        "output_description": "Print `Hello, World!` on a single line.",
        "difficulty": "Low",
        "samples": [
            {"input": "", "output": "Hello, World!\n"}
        ],
        "cases": [
            ("", "Hello, World!\n"),
        ],
    },
    {
        "_id": "SUMN",
        "title": "Sum 1 to N",
        "description": "Given a positive integer $N$, compute the sum of all integers from $1$ to $N$, i.e. $1 + 2 + \\dots + N$.",
        "input_description": "A single line containing an integer $N$ ($1 \\le N \\le 10^4$).",
        "output_description": "Print a single integer representing the sum.",
        "difficulty": "Low",
        "samples": [
            {"input": "5\n", "output": "15\n"}
        ],
        "cases": [
            ("5\n", "15\n"),
            ("1\n", "1\n"),
            ("10\n", "55\n"),
            ("100\n", "5050\n"),
            ("1000\n", "500500\n"),
        ],
    },
    {
        "_id": "APLUSB",
        "title": "A + B Problem",
        "description": "Given two integers $A$ and $B$, compute their sum $A + B$.",
        "input_description": "A single line containing two space-separated integers $A$ and $B$ ($-10^9 \\le A, B \\le 10^9$).",
        "output_description": "Print a single integer representing $A + B$.",
        "difficulty": "Low",
        "samples": [
            {"input": "1 2\n", "output": "3\n"}
        ],
        "cases": [
            ("1 2\n", "3\n"),
            ("-5 10\n", "5\n"),
            ("0 0\n", "0\n"),
            ("1000 -1000\n", "0\n"),
            ("123456 654321\n", "777777\n"),
        ],
    },
    {
        "_id": "MAXOF3",
        "title": "Maximum of Three Numbers",
        "description": "Given three integers, find and print the maximum value among them.",
        "input_description": "A single line containing three space-separated integers $A$, $B$, and $C$ ($-10^9 \\le A, B, C \\le 10^9$).",
        "output_description": "Print the maximum of the three integers.",
        "difficulty": "Low",
        "samples": [
            {"input": "1 2 3\n", "output": "3\n"}
        ],
        "cases": [
            ("1 2 3\n", "3\n"),
            ("10 5 8\n", "10\n"),
            ("-3 -7 -1\n", "-1\n"),
            ("42 42 42\n", "42\n"),
            ("0 -10 5\n", "5\n"),
        ],
    },
    {
        "_id": "STRREV",
        "title": "Reverse a String",
        "description": "Given a single string on one line, output the reversed string.",
        "input_description": "A single non-empty line containing a string of printable non-whitespace characters (length $\\le 1000$).",
        "output_description": "Print the reversed string.",
        "difficulty": "Low",
        "samples": [
            {"input": "hello\n", "output": "olleh\n"}
        ],
        "cases": [
            ("hello\n", "olleh\n"),
            ("world\n", "dlrow\n"),
            ("a\n", "a\n"),
            ("racecar\n", "racecar\n"),
            ("Cangjie\n", "eijgnaC\n"),
        ],
    },
    {
        "_id": "FACTORIAL",
        "title": "Factorial",
        "description": "Given a non-negative integer $N$ ($0 \\le N \\le 12$), compute its factorial $N! = 1 \\times 2 \\times \\dots \\times N$, with $0! = 1$.",
        "input_description": "A single line containing an integer $N$ ($0 \\le N \\le 12$).",
        "output_description": "Print the value of $N!$.",
        "difficulty": "Low",
        "samples": [
            {"input": "5\n", "output": "120\n"}
        ],
        "cases": [
            ("0\n", "1\n"),
            ("1\n", "1\n"),
            ("5\n", "120\n"),
            ("10\n", "3628800\n"),
            ("12\n", "479001600\n"),
        ],
    },
    {
        "_id": "FIBONACCI",
        "title": "Fibonacci Number",
        "description": "Compute the $n$-th Fibonacci number $F(n)$, where $F(0) = 0$, $F(1) = 1$, and $F(n) = F(n-1) + F(n-2)$ for $n \\ge 2$.",
        "input_description": "A single line containing an integer $n$ ($0 \\le n \\le 40$).",
        "output_description": "Print the value of $F(n)$.",
        "difficulty": "Low",
        "samples": [
            {"input": "6\n", "output": "8\n"}
        ],
        "cases": [
            ("0\n", "0\n"),
            ("1\n", "1\n"),
            ("6\n", "8\n"),
            ("15\n", "610\n"),
            ("30\n", "832040\n"),
            ("40\n", "102334155\n"),
        ],
    },
    {
        "_id": "GCDLCM",
        "title": "GCD and LCM",
        "description": "Given two positive integers $A$ and $B$, compute their Greatest Common Divisor (GCD) and Least Common Multiple (LCM).",
        "input_description": "A single line containing two space-separated positive integers $A$ and $B$ ($1 \\le A, B \\le 10^9$).",
        "output_description": "Print two space-separated integers: the GCD followed by the LCM.",
        "difficulty": "Low",
        "samples": [
            {"input": "12 18\n", "output": "6 36\n"}
        ],
        "cases": [
            ("12 18\n", "6 36\n"),
            ("7 13\n", "1 91\n"),
            ("15 15\n", "15 15\n"),
            ("24 60\n", "12 120\n"),
            ("100 25\n", "25 100\n"),
        ],
    },
    {
        "_id": "PRIMETEST",
        "title": "Prime Number Test",
        "description": "Given an integer $N$, determine whether it is a prime number. Print `Yes` if it is prime, or `No` otherwise.",
        "input_description": "A single line containing an integer $N$ ($1 \\le N \\le 10^9$).",
        "output_description": "Print `Yes` if $N$ is prime, or `No` if $N$ is not prime.",
        "difficulty": "Low",
        "samples": [
            {"input": "17\n", "output": "Yes\n"}
        ],
        "cases": [
            ("1\n", "No\n"),
            ("2\n", "Yes\n"),
            ("17\n", "Yes\n"),
            ("100\n", "No\n"),
            ("999983\n", "Yes\n"),
            ("1000000000\n", "No\n"),
        ],
    },
    {
        "_id": "ARREXTREMES",
        "title": "Array Sum and Extremes",
        "description": "Given an array of $N$ integers, calculate the sum, the minimum element, and the maximum element.",
        "input_description": "The first line contains an integer $N$ ($1 \\le N \\le 1000$). The second line contains $N$ space-separated integers ($-10^6 \\le A_i \\le 10^6$).",
        "output_description": "Print three space-separated integers: sum, minimum, and maximum.",
        "difficulty": "Low",
        "samples": [
            {"input": "5\n1 2 3 4 5\n", "output": "15 1 5\n"}
        ],
        "cases": [
            ("5\n1 2 3 4 5\n", "15 1 5\n"),
            ("4\n-10 0 20 -5\n", "5 -10 20\n"),
            ("1\n42\n", "42 42 42\n"),
            ("6\n-1 -2 -3 -4 -5 -6\n", "-21 -6 -1\n"),
        ],
    },
    {
        "_id": "PALINDROME",
        "title": "Palindrome String",
        "description": "Given a string of characters without whitespace, determine if it reads the same forward and backward. Comparison is case-sensitive.",
        "input_description": "A single non-empty line containing a string of at most 1000 characters.",
        "output_description": "Print `Yes` if the string is a palindrome, or `No` otherwise.",
        "difficulty": "Low",
        "samples": [
            {"input": "racecar\n", "output": "Yes\n"}
        ],
        "cases": [
            ("level\n", "Yes\n"),
            ("Hello\n", "No\n"),
            ("a\n", "Yes\n"),
            ("racecar\n", "Yes\n"),
            ("abccba\n", "Yes\n"),
            ("abcdecba\n", "No\n"),
        ],
    },
    {
        "_id": "SORTINTS",
        "title": "Sort Integers",
        "description": "Given $N$ integers, sort them in non-decreasing (ascending) order.",
        "input_description": "The first line contains an integer $N$ ($1 \\le N \\le 1000$). The second line contains $N$ space-separated integers ($-10^9 \\le A_i \\le 10^9$).",
        "output_description": "Print the sorted integers on a single line, separated by spaces.",
        "difficulty": "Low",
        "samples": [
            {"input": "5\n5 3 1 4 2\n", "output": "1 2 3 4 5\n"}
        ],
        "cases": [
            ("5\n5 3 1 4 2\n", "1 2 3 4 5\n"),
            ("3\n10 -5 0\n", "-5 0 10\n"),
            ("1\n99\n", "99\n"),
            ("6\n2 2 1 3 1 2\n", "1 1 2 2 2 3\n"),
        ],
    },
    {
        "_id": "VOWELCOUNT",
        "title": "Count Vowels and Consonants",
        "description": "Given a non-empty string consisting only of lowercase English letters (`a`-`z`), count the total number of vowels (`a`, `e`, `i`, `o`, `u`) and consonants.",
        "input_description": "A single line containing a non-empty string of lowercase English letters (length $\\le 1000$).",
        "output_description": "Print two space-separated integers: the number of vowels followed by the number of consonants.",
        "difficulty": "Low",
        "samples": [
            {"input": "hello\n", "output": "2 3\n"}
        ],
        "cases": [
            ("hello\n", "2 3\n"),
            ("aeiou\n", "5 0\n"),
            ("rhythm\n", "0 6\n"),
            ("cangjielanguage\n", "7 8\n"),
            ("xyz\n", "0 3\n"),
        ],
    },
    {
        "_id": "BINSEARCH",
        "title": "Binary Search",
        "description": "Given a sorted array of $N$ distinct integers in ascending order and a target integer $K$, find the 0-based index of $K$ in the array. If $K$ is not present, print `-1`.",
        "input_description": "The first line contains two integers $N$ ($1 \\le N \\le 10^5$) and $K$ ($-10^9 \\le K \\le 10^9$). The second line contains $N$ space-separated sorted distinct integers.",
        "output_description": "Print the 0-based index of $K$, or `-1` if not found.",
        "difficulty": "Mid",
        "samples": [
            {"input": "5 7\n1 3 5 7 9\n", "output": "3\n"}
        ],
        "cases": [
            ("5 7\n1 3 5 7 9\n", "3\n"),
            ("5 4\n1 3 5 7 9\n", "-1\n"),
            ("1 10\n10\n", "0\n"),
            ("6 -5\n-10 -5 0 5 10 15\n", "1\n"),
            ("4 20\n1 2 3 4\n", "-1\n"),
        ],
    },
    {
        "_id": "MATRIXTRANS",
        "title": "Matrix Transposition",
        "description": "Given an $R \\times C$ matrix of integers, compute and print its transpose (a $C \\times R$ matrix where rows become columns).",
        "input_description": "The first line contains two integers $R$ and $C$ ($1 \\le R, C \\le 100$). The next $R$ lines each contain $C$ space-separated integers.",
        "output_description": "Print $C$ lines, each containing $R$ space-separated integers representing the transposed matrix.",
        "difficulty": "Mid",
        "samples": [
            {"input": "2 3\n1 2 3\n4 5 6\n", "output": "1 4\n2 5\n3 6\n"}
        ],
        "cases": [
            ("2 3\n1 2 3\n4 5 6\n", "1 4\n2 5\n3 6\n"),
            ("1 3\n10 20 30\n", "10\n20\n30\n"),
            ("2 2\n1 0\n0 1\n", "1 0\n0 1\n"),
            ("3 1\n7\n8\n9\n", "7 8 9\n"),
        ],
    },
    {
        "_id": "PARENMATCH",
        "title": "Valid Parentheses",
        "description": "Given a string containing only bracket characters `(`, `)`, `[`, `]`, `{`, and `}`, determine if the bracket sequence is valid. A sequence is valid if open brackets are closed by the same type of brackets and in the correct order.",
        "input_description": "A single non-empty line containing brackets (length $\\le 10^4$).",
        "output_description": "Print `Valid` if the bracket string is valid, or `Invalid` otherwise.",
        "difficulty": "Mid",
        "samples": [
            {"input": "()[]{}\n", "output": "Valid\n"}
        ],
        "cases": [
            ("()[]{}\n", "Valid\n"),
            ("(]\n", "Invalid\n"),
            ("([{}])\n", "Valid\n"),
            ("([)]\n", "Invalid\n"),
            ("{\n", "Invalid\n"),
            ("()\n", "Valid\n"),
        ],
    },
    {
        "_id": "MAXSUBARR",
        "title": "Maximum Subarray Sum",
        "description": "Given an array of $N$ integers, find the contiguous subarray (containing at least one number) which has the largest sum and print that sum.",
        "input_description": "The first line contains an integer $N$ ($1 \\le N \\le 10^5$). The second line contains $N$ space-separated integers ($-10^4 \\le A_i \\le 10^4$).",
        "output_description": "Print a single integer representing the maximum subarray sum.",
        "difficulty": "Mid",
        "samples": [
            {"input": "9\n-2 1 -3 4 -1 2 1 -5 4\n", "output": "6\n"}
        ],
        "cases": [
            ("9\n-2 1 -3 4 -1 2 1 -5 4\n", "6\n"),
            ("5\n-1 -2 -3 -4 -5\n", "-1\n"),
            ("1\n100\n", "100\n"),
            ("5\n5 4 -1 7 8\n", "23\n"),
        ],
    },
    {
        "_id": "COINCHANGE",
        "title": "Coin Change",
        "description": "Given $N$ distinct coin denominations and a target amount $M$, find the minimum number of coins needed to make up that amount. If the amount cannot be made up by any combination of the coins, print `-1`. You may use an unlimited number of each coin denomination.",
        "input_description": "The first line contains two integers $N$ ($1 \\le N \\le 50$) and $M$ ($0 \\le M \\le 10000$). The second line contains $N$ space-separated integers representing the coin denominations.",
        "output_description": "Print the minimum number of coins needed, or `-1` if impossible.",
        "difficulty": "Mid",
        "samples": [
            {"input": "3 11\n1 2 5\n", "output": "3\n"}
        ],
        "cases": [
            ("3 11\n1 2 5\n", "3\n"),
            ("1 3\n2\n", "-1\n"),
            ("1 0\n1\n", "0\n"),
            ("4 6249\n186 419 83 408\n", "20\n"),
            ("3 7\n2 4 6\n", "-1\n"),
        ],
    },
    {
        "_id": "LCS",
        "title": "Longest Common Subsequence",
        "description": "Given two strings $S$ and $T$, find the length of their Longest Common Subsequence (LCS).",
        "input_description": "The first line contains string $S$. The second line contains string $T$. Both strings consist of uppercase English letters (lengths between 1 and 1000).",
        "output_description": "Print a single integer representing the length of the longest common subsequence.",
        "difficulty": "High",
        "samples": [
            {"input": "ABCBDAB\nBDCABA\n", "output": "4\n"}
        ],
        "cases": [
            ("ABCBDAB\nBDCABA\n", "4\n"),
            ("ABC\nDEF\n", "0\n"),
            ("AGGTAB\nGXTXAYB\n", "4\n"),
            ("AAAA\nAA\n", "2\n"),
            ("PROGRAMMING\nGAMING\n", "6\n"),
        ],
    },
    {
        "_id": "KNAPSACK01",
        "title": "0-1 Knapsack Problem",
        "description": "You have $N$ items, each with a weight $w_i$ and a value $v_i$, and a knapsack with maximum weight capacity $W$. Find the maximum total value of items you can put into the knapsack without exceeding capacity $W$. Each item can be included at most once.",
        "input_description": "The first line contains two integers $N$ and $W$ ($1 \\le N \\le 1000, 1 \\le W \\le 1000$). The next $N$ lines each contain two space-separated integers $w_i$ and $v_i$ ($1 \\le w_i, v_i \\le 1000$).",
        "output_description": "Print a single integer representing the maximum achievable total value.",
        "difficulty": "High",
        "samples": [
            {"input": "3 4\n1 15\n3 20\n4 30\n", "output": "35\n"}
        ],
        "cases": [
            ("3 4\n1 15\n3 20\n4 30\n", "35\n"),
            ("4 5\n2 3\n3 4\n4 5\n5 6\n", "7\n"),
            ("3 3\n4 10\n5 20\n6 30\n", "0\n"),
            ("1 10\n5 50\n", "50\n"),
        ],
    },
    {
        "_id": "TWOSUM",
        "title": "Two Sum",
        "description": "Given an array of $N$ integers and an integer target $T$, find the 0-based indices of the two numbers such that they add up to $T$. Output the two indices separated by a space in ascending order ($i < j$). If no such pair exists, print `-1`.",
        "input_description": "The first line contains two integers $N$ ($2 \\le N \\le 10^5$) and $T$ ($-10^9 \\le T \\le 10^9$). The second line contains $N$ space-separated integers.",
        "output_description": "Print two space-separated indices $i$ and $j$ ($i < j$), or `-1`.",
        "difficulty": "Low",
        "samples": [
            {"input": "4 9\n2 7 11 15\n", "output": "0 1\n"}
        ],
        "cases": [
            ("4 9\n2 7 11 15\n", "0 1\n"),
            ("3 6\n3 2 4\n", "1 2\n"),
            ("2 6\n3 3\n", "0 1\n"),
            ("4 100\n1 2 3 4\n", "-1\n"),
            ("5 0\n-5 2 7 8 5\n", "0 4\n"),
        ],
    },
    {
        "_id": "CLIMBSTAIRS",
        "title": "Climbing Stairs",
        "description": "You are climbing a staircase. It takes $N$ steps to reach the top. Each time you can either climb $1$ or $2$ steps. In how many distinct ways can you climb to the top?",
        "input_description": "A single line containing an integer $N$ ($1 \\le N \\le 45$).",
        "output_description": "Print the number of distinct ways to reach the top.",
        "difficulty": "Low",
        "samples": [
            {"input": "3\n", "output": "3\n"}
        ],
        "cases": [
            ("1\n", "1\n"),
            ("2\n", "2\n"),
            ("3\n", "3\n"),
            ("5\n", "8\n"),
            ("10\n", "89\n"),
            ("35\n", "14930352\n"),
        ],
    },
    {
        "_id": "FIZZBUZZ",
        "title": "FizzBuzz",
        "description": "Given an integer $N$, output the strings from $1$ to $N$ separated by space where:\n- For multiples of 3 and 5, print `FizzBuzz`\n- For multiples of 3, print `Fizz`\n- For multiples of 5, print `Buzz`\n- For any other number, print the number itself.",
        "input_description": "A single line containing an integer $N$ ($1 \\le N \\le 1000$).",
        "output_description": "Print $N$ space-separated tokens on a single line.",
        "difficulty": "Low",
        "samples": [
            {"input": "5\n", "output": "1 2 Fizz 4 Buzz\n"}
        ],
        "cases": [
            ("1\n", "1\n"),
            ("3\n", "1 2 Fizz\n"),
            ("5\n", "1 2 Fizz 4 Buzz\n"),
            ("15\n", "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz\n"),
        ],
    },
    {
        "_id": "VALIDANAG",
        "title": "Valid Anagram",
        "description": "Given two strings $S$ and $T$ of lowercase English letters, determine if $T$ is an anagram of $S$ (contains exactly the same characters with the same frequencies). Print `Yes` or `No`.",
        "input_description": "The first line contains string $S$. The second line contains string $T$ (lengths $\\le 10^5$).",
        "output_description": "Print `Yes` if $T$ is an anagram of $S$, or `No` otherwise.",
        "difficulty": "Low",
        "samples": [
            {"input": "anagram\nnagaram\n", "output": "Yes\n"}
        ],
        "cases": [
            ("anagram\nnagaram\n", "Yes\n"),
            ("rat\ncar\n", "No\n"),
            ("listen\nsilent\n", "Yes\n"),
            ("a\nab\n", "No\n"),
            ("cangjie\neijgnac\n", "Yes\n"),
        ],
    },
    {
        "_id": "STOCKPROFIT",
        "title": "Best Time to Buy and Sell Stock",
        "description": "You are given an array $P$ where $P_i$ is the price of a given stock on the $i$-th day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve. If you cannot achieve any profit, return 0.",
        "input_description": "The first line contains an integer $N$ ($1 \\le N \\le 10^5$). The second line contains $N$ space-separated integers ($0 \\le P_i \\le 10^4$).",
        "output_description": "Print the maximum profit achievable.",
        "difficulty": "Low",
        "samples": [
            {"input": "6\n7 1 5 3 6 4\n", "output": "5\n"}
        ],
        "cases": [
            ("6\n7 1 5 3 6 4\n", "5\n"),
            ("5\n7 6 4 3 1\n", "0\n"),
            ("2\n2 4\n", "2\n"),
            ("1\n5\n", "0\n"),
            ("5\n1 2 3 4 5\n", "4\n"),
        ],
    },
    {
        "_id": "LONGESTSUBSTR",
        "title": "Longest Substring Without Repeating Characters",
        "description": "Given a string $S$, find the length of the longest substring without repeating characters.",
        "input_description": "A single line containing string $S$ (length $\\le 10^4$, printable characters).",
        "output_description": "Print the maximum length of a substring without repeating characters.",
        "difficulty": "Mid",
        "samples": [
            {"input": "abcabcbb\n", "output": "3\n"}
        ],
        "cases": [
            ("abcabcbb\n", "3\n"),
            ("bbbbb\n", "1\n"),
            ("pwwkew\n", "3\n"),
            ("abcdef\n", "6\n"),
            ("a\n", "1\n"),
        ],
    },
    {
        "_id": "MERGEINTERVALS",
        "title": "Merge Overlapping Intervals",
        "description": "Given an array of $N$ intervals $[\\text{start}_i, \\text{end}_i]$, merge all overlapping intervals, and output the merged intervals sorted by start time.",
        "input_description": "The first line contains an integer $N$ ($1 \\le N \\le 10^4$). The next $N$ lines each contain two integers: $\\text{start}_i$ and $\\text{end}_i$ ($-10^9 \\le \\text{start}_i \\le \\text{end}_i \\le 10^9$).",
        "output_description": "Print the merged intervals, one per line, formatted as `start end`.",
        "difficulty": "Mid",
        "samples": [
            {"input": "4\n1 3\n2 6\n8 10\n15 18\n", "output": "1 6\n8 10\n15 18\n"}
        ],
        "cases": [
            ("4\n1 3\n2 6\n8 10\n15 18\n", "1 6\n8 10\n15 18\n"),
            ("2\n1 4\n4 5\n", "1 5\n"),
            ("3\n6 8\n1 9\n2 4\n", "1 9\n"),
            ("1\n5 10\n", "5 10\n"),
        ],
    },
    {
        "_id": "ROTIMG",
        "title": "Rotate Matrix 90 Degrees Clockwise",
        "description": "You are given an $N \\times N$ 2D matrix representing an image. Rotate the image clockwise by 90 degrees.",
        "input_description": "The first line contains an integer $N$ ($1 \\le N \\le 100$). The next $N$ lines each contain $N$ space-separated integers.",
        "output_description": "Print $N$ lines, each containing $N$ space-separated integers of the rotated matrix.",
        "difficulty": "Mid",
        "samples": [
            {"input": "3\n1 2 3\n4 5 6\n7 8 9\n", "output": "7 4 1\n8 5 2\n9 6 3\n"}
        ],
        "cases": [
            ("3\n1 2 3\n4 5 6\n7 8 9\n", "7 4 1\n8 5 2\n9 6 3\n"),
            ("2\n1 2\n3 4\n", "3 1\n4 2\n"),
            ("1\n42\n", "42\n"),
        ],
    },
    {
        "_id": "TRAPPINGRAIN",
        "title": "Trapping Rain Water",
        "description": "Given $N$ non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.",
        "input_description": "The first line contains an integer $N$ ($1 \\le N \\le 10^5$). The second line contains $N$ space-separated non-negative integers ($0 \\le H_i \\le 10^4$).",
        "output_description": "Print the total amount of trapped water.",
        "difficulty": "High",
        "samples": [
            {"input": "12\n0 1 0 2 1 0 1 3 2 1 2 1\n", "output": "6\n"}
        ],
        "cases": [
            ("12\n0 1 0 2 1 0 1 3 2 1 2 1\n", "6\n"),
            ("6\n4 2 0 3 2 5\n", "9\n"),
            ("3\n3 0 2\n", "2\n"),
            ("2\n1 2\n", "0\n"),
            ("5\n1 1 1 1 1\n", "0\n"),
        ],
    },
    {
        "_id": "LIS",
        "title": "Longest Increasing Subsequence",
        "description": "Given an integer array of length $N$, return the length of the longest strictly increasing subsequence.",
        "input_description": "The first line contains an integer $N$ ($1 \\le N \\le 2500$). The second line contains $N$ space-separated integers ($-10^4 \\le A_i \\le 10^4$).",
        "output_description": "Print a single integer representing the length of the longest strictly increasing subsequence.",
        "difficulty": "High",
        "samples": [
            {"input": "8\n10 9 2 5 3 7 101 18\n", "output": "4\n"}
        ],
        "cases": [
            ("8\n10 9 2 5 3 7 101 18\n", "4\n"),
            ("6\n0 1 0 3 2 3\n", "4\n"),
            ("7\n7 7 7 7 7 7 7\n", "1\n"),
            ("1\n42\n", "1\n"),
            ("5\n1 3 6 7 9\n", "5\n"),
        ],
    },
]
