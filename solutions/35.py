# 35. Search Insert Position
#
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
# return the index where it would be if it were inserted in order.

def binarySearch(arr, ele):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == ele:
            return mid
        elif arr[mid] > ele:
            high = mid - 1
        elif arr[mid] < ele:
            low = mid + 1
    return low
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return binarySearch(nums,target)