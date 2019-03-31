#https://leetcode.com/problems/contains-duplicate/
class Solution(object):
    def containsDuplicate(self, nums):
        return max(collections.Counter(nums).values()+[0]) >1 
