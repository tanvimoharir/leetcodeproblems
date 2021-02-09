# 240. Search a 2D Matrix II
# Solution Accepted :160ms Faster than 85 percent


def binarysearch(arr,target):
    low=0
    high=len(arr)-1
    result=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            high=mid-1
        elif arr[mid]<target:
            low=mid+1
    return result
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for array in matrix:
            if target==array[0] or target==array[-1] or target==array[len(array)//2]:
                return True
            else:
                result=binarysearch(array,target)
                if result!=-1:
                    return result
        return False
