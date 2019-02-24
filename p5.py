#https://leetcode.com/problems/remove-element/
#visit the abve link to see the problem description
class Solution:
    def removeElement(self, nums: 'List[int]', val: 'int') -> 'int':
        n=len(nums)
        for i in range(n-1,-1,-1):
            if nums[i]==val:
                del nums[i]
                
        return len(nums)        
