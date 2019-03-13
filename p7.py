#https://leetcode.com/problems/search-insert-position/
#visit the above link to see problem  description
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        h=len(nums)-1
        l=0
        while l<=h :
            mid=(h+l)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                h=mid-1
            else:l=mid+1
                
        return l
