#https://leetcode.com/problems/excel-sheet-column-title/
class Solution:
    def convertToTitle(self, n: int) -> str:
        d='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        r=''
        while n>0:
            n=n-1
            r=d[n%26]+r
            n=n//26
        return r
