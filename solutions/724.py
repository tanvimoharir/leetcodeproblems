# 724. Find Pivot Index

# Given an array of integers nums, write a method that returns the "pivot" index of this array.
# We define the pivot index as the index where the sum of all the numbers to the left of the index is equal to the
# sum of all the numbers to the right of the index.
# If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most
# pivot index.

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for i in range(len(nums)):
            left_sum += nums[i]
            if left_sum == right_sum:
                return i
            right_sum -= nums[i]
        return -1
