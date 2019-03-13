#https://leetcode.com/problems/implement-strstr/
#visit the above link to see problem description
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        else:
            n=len(needle)
            for i in range(len(haystack)):
                if(haystack[i:i+n]==needle):
                    return i
            return -1
