#https://leetcode.com/problems/two-sum/
#click the above link to see the problem definition
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for idx,e in enumerate(nums):
            if target-e in m:
                return [m[target-e],idx]
            m[e]=idx
