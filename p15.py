#https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        h,j={},0
        for i in nums:
            if i not in h:
                h.update({i:j})
                j=j+1
            else:h.pop(i)
        k=list(h.keys())
        return k[0]
