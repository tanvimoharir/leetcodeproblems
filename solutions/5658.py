# 5658. Maximum Absolute Sum of Any Subarray
# Biweekly contest 45

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        currentmax = globalmax = currentmin = nums[0]
        for i in range(1, len(nums)):
            x, y = nums[i] + currentmax, nums[i] + currentmin
            currentmax = max(nums[i], x, y)
            currentmin = min(nums[i], x, y)
            globalmax = max(globalmax, abs(currentmax), abs(currentmin))
        return globalmax
