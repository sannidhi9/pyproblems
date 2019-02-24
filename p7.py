#https://leetcode.com/problems/search-insert-position/
#visit the above link to see problem  description
class Solution:
    def searchInsert(self, nums: 'List[int]', target: 'int') -> 'int':
        if len(nums)==1 and target<nums[0]:
            return 0
        elif len(nums)==1 and target>nums[0]:
            return 1
        elif len(nums)==1 and target==nums[0]:
            return 0
            
        for i in range(len(nums)-1):
            if nums[i]==target:
                return i
            elif target<nums[i] and i==0:
                return 0
            elif target>nums[i] and target<nums[i+1]:
                return i+1
            
            
            if (i+1)==len(nums)-1 and target==nums[i+1]:
                return i+1
            elif (i+1)==len(nums)-1 and target<nums[i+1]:
                return i
            elif (i+1)==len(nums)-1 and target>nums[i+1]:
                return i+2            
