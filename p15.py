#https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        h=[]
        for i in nums:
            if i not in h:
                h=h+[i]
            else :h.remove(i)
        return h[0]
