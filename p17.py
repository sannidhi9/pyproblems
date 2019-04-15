#https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            if nums[i] not in list(d.values()):
                d.update({nums.count(nums[i]):nums[i]})
        return d[max(list(d.keys()))]
