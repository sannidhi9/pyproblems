#https://leetcode.com/problems/length-of-last-word/
#visit the above link to see problem description
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x=s.split()
        if len(s)!=0 and len(x)!=0:
            return len(x[len(x)-1])
        else:return 0
