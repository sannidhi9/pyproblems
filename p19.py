#https://leetcode.com/problems/rotate-array/submissions/
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums_copy = nums.copy()
        for i in range(0, len(nums)):
            nums[(i+k) % len(nums)] = nums_copy[i]
