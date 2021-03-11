# solution adapted from https://www.youtube.com/watch?v=oBt53YbR9Kk
def bestSum(coins,amount,memo):
    if amount in memo:
        return memo[amount]
    if  amount==0:
        return []
    if amount<0:
        return -1
    current_max=-1
    for coin in coins:
        result=bestSum(coins,amount-coin,memo)
        if result!=-1:
            result=result+[coin]
            if current_max==-1 or len(result)<len(current_max):
                current_max=result
    memo[amount]=current_max
    return memo[amount]

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        val= bestSum(coins,amount,memo={})
        if val!=-1:
            return len(val)
        return val
