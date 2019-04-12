#https://leetcode.com/problems/merge-sorted-array/
#visit th eabove link to see problem definition
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k = m + n-1
        i, j =m - 1,n - 1
        while i>= 0 or j>= 0:
            if i < 0:
                nums1[k]=nums2[j]
                j=j-1
            elif j < 0:
                nums1[k]=nums1[i]
                i=i-1
            elif nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i=i-1
            else: 
                nums1[k]=nums2[j]
                j=j-1
            k=k-1
