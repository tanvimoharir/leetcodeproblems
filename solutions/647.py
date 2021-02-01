# 647. Palindromic Substrings
# Leetcode Solutions
# Approach #1: Check All Substrings (Time limit exceeded)

def isPalindrome(s, low, high):
    while low < high:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1
    return True


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for low in range(len(s)):
            for high in range(low, len(s)):
                count += isPalindrome(s, low, high)
        return count

# Approach #2: Dynamic Programming(Accepted)

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        if n <= 0:
            return 0
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            count += 1
        for i in range(n - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
            count += dp[i][i + 1]
        for l in range(3, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                count += dp[i][j]
        return count

# Approach #3: Expand Around Possible Centers(Accepted)

def countPalindromesAroundCenter(s, low, high):
    count = 0
    while low >= 0 and high < len(s):
        if s[low] != s[high]:
            break
        # expand around center
        low -= 1
        high += 1
        count += 1
    return count


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            # odd length palindroms,single character center
            count += countPalindromesAroundCenter(s, i, i)

            # even length palindromes,consecutive characters center
            count += countPalindromesAroundCenter(s, i, i + 1)

        return count
