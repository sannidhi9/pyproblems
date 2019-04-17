#https://leetcode.com/problems/excel-sheet-column-number/
class Solution:
    def titleToNumber(self, s: str) -> int:
        if len(s)==1:
            return ord(s[0])-64
        r=ord(s[0])-64
        for i in range(len(s)-1):
            r=r*26+ord(s[i+1])-64
        return r
