#https://leetcode.com/problems/number-of-1-bits/
class Solution(object):
    def hammingWeight(self, n):
        s,count=bin(n),0
        s=str(s)
        for i in range(len(s)):
            if s[i]=='1':
                count=count+1
        return count
