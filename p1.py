#https://leetcode.com/problems/two-sum/
#click the above link to see the problem definition
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        b={}
        for i in range(len(nums)):
            c={nums[i]:i}
            b.update(c)
        for j in range(len(nums)-1):
            if (target-nums[j]) in b and j!=b[target-nums[j]]:
                return [j,b[target-nums[j]]]

