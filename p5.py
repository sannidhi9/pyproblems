#https://leetcode.com/problems/remove-element/
#visit the abve link to see the problem description
class Solution:
    def removeElement(self, nums: 'List[int]', val: 'int') -> 'int':
        count=0
        if len(nums)==1 and nums[0]==val:
            return 0
        elif len(nums)==1 and nums[0]!=val:
            return 1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==val:
                count=count+1
                for j in range(i,len(nums)-1):
                    temp=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp  
        return len(nums)-count
