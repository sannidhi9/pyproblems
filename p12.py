#https://leetcode.com/problems/merge-sorted-array/
#visit th eabove link to see problem definition
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(len(nums2)):
            nums1[m]=nums2[i]
            m=m+1
        nums1.sort() 
