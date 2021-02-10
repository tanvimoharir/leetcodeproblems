# 33. Search in Rotated Sorted Array solution improvised per
# https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14425/Concise-O(log-N)-Binary-search-solution
def binarysearch(array,target,pivotindex):
    low=0
    high=len(array)-1
    result=-1
    while low<=high:
        mid=(low+high)//2
        realmid=(mid+pivotindex)%len(array)
        if array[realmid]==target:
            return realmid
        elif array[realmid]>target:
            high=mid-1
        elif array[realmid]<target:
            low=mid+1
    return result
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivotelement=min(nums)
        pivotindex=nums.index(pivotelement)
        return binarysearch(nums,target,pivotindex)