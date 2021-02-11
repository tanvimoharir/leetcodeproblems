# 5. Longest Palindromic Substring
# Leetcode solution (Approach 5:Expand around centers)

def expandAroundCenter(s,left,right):
    l,r=left,right
    while l>=0 and r<len(s) and s[l]==s[r]:
        l-=1
        r+=1
    return r-l-1
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s)<1:
            return ""
        start=end=0
        for i in range(len(s)):
            len1=expandAroundCenter(s,i,i)
            len2=expandAroundCenter(s,i,i+1)
            lens=max(len1,len2)
            if lens>end-start:
                start=i-(lens-1)//2
                end=i+lens//2
        return s[start:end+1]

