#https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=collections.Counter(nums)
        b=max(d.values())
        key_list = list(d.keys()) 
        val_list = list(d.values()) 
        return (key_list[val_list.index(b)])
