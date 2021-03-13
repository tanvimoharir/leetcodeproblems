
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
      
# Leetcode solution approach 2 : Rolling hash
class Solution:
     def hasAllCodes(self, s: str, k: int) -> bool:
        need=1<<k
        got=[False]*need
        all_one=need-1
        hash_val=0
        for i in range(len(s)):
            #calculating hash for s[i-k+1:i+1]
            hash_val=((hash_val<<1)&all_one)|(int(s[i]))
            
            #hash only available when i-k+1>0
            if i>=k-1 and got[hash_val] is False:
                got[hash_val]=True
                need-=1
                if need==0:
                    return True
        return False
      
