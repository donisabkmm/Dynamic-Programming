"""
Given a string s, return the longest
palindromic
substring
in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

Solution:
1. Brute Force way:
 Here we have to check all every single substring of s and check
 it's a palindrome and get the longest one

 In this method we have to check every substring of s to check whether it's a palindrome
 so that it's going to take linear time complexity.
 This method has a time complexity of O(n3)O(n3) because generating all substrings takes O(n2)O(n2) time, and
 checking if each substring is a palindrome takes O(n)O(n) time.
 n*n^2  so overall time complexity is O(n^3)


2. DP Way:
 Here we can check the outside substring are equal and the middle substring is single then it a palindrome.
 Also, suppose we choose a substring and lhs and rhs are equal then also we can conclude it's a palindrome,
 So that the time complexity of this approach is n*n that means o(n^2)


Let's start the coding part

"""

def longestPalindrome(s) :
    def is_palindrome(sub: str) -> bool:
        return sub == sub[::-1]

    n = len(s)
    if n == 0:
        return ""

    longest_palindrome = ""

    for i in range(n):
        for j in range(i, n):
            substring = s[i:j + 1]
            if is_palindrome(substring) and len(substring) > len(longest_palindrome):
                longest_palindrome = substring

    return longest_palindrome


def longestPalindromeDP( s: str) -> str:
    res = ""
    reslen = 0

    for i in range(len(s)):
        # Odd length palindromes
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > reslen:
                res = s[l:r + 1]
                reslen = r - l + 1
            l -= 1
            r += 1

        # Even length palindromes
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > reslen:
                res = s[l:r + 1]
                reslen = r - l + 1
            l -= 1
            r += 1

    return res




"""Testcases"""

test_cases = [{"test":["babad","bab"]},{"test":["cbbd","bb"]}]

for testcase in test_cases:
    bruteforce = longestPalindrome(testcase["test"][0])
    if bruteforce == testcase["test"][1]:
        print(f"Passed using BruteForce {bruteforce}")

for testcase in test_cases:
    Dp = longestPalindromeDP(testcase["test"][0])
    if Dp == testcase["test"][1]:
        print(f"Passed using DP {Dp}")