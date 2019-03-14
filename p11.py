#https://leetcode.com/problems/sqrtx/
#visit the above link to see problem definition
class Solution:
    def mySqrt(self, x: int) -> int:
        i=1
        while i*i<=x:
            i=i+1
        return i-1 
