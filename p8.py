#https://leetcode.com/problems/length-of-last-word/
#visit the above link to see problem description
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=0
        b=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ':
                c=c+1
            else:break
        for i in range(len(s)-1-c,-1,-1):
            if s[i]==' ':
                break
            b=b+1
        return b
