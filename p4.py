#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#visit the above link to see problem definition
class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        count=0
        for i in range(len(nums)-1,0,-1):
            if nums[i]==nums[i-1]:
                j=0
                count=count+1
                for j in range(i,len(nums)-1):
                    nums[j]=nums[j+1]    
        return len(nums)-count

