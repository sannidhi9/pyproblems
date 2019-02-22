#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        n=len(nums)-1
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                del nums[i]
                n=n-1

        return nums
