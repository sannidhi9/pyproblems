#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        nums=list(map(int,nums))
        n=len(nums)-1
        for i in range(n):
            for j in range(n):
                x=nums[i]
                y=nums[j]
                if int(x)==int(y) and i!=j:
                    del nums[j]
                    n=n-1

        return nums
