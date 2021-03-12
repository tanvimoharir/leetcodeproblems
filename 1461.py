# 1461. Check If a String Contains All Binary Codes of Size K
# Leetcode approach 1 
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need=1<<k
        got=set()
        start,end=0,0
        while end<len(s):
            if end-start+1<k:
                end+=1
            if end-start+1==k:
                tmp=s[start:end+1]
                if tmp not in got:
                    got.add(tmp)
                    need-=1
                    if need==0:
                        return True
                start+=1
                end+=1
        return False
