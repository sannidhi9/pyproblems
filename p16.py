#https://leetcode.com/problems/excel-sheet-column-title/
class Solution:
    def convertToTitle(self, n: int) -> str:
        d='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        r=[]
        while n>0:
            n=n-1
            r.append(d[n%26])
            n=n//26
        return ''.join(r[::-1])
