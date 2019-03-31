#https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        r1=''.join(sorted(s))
        r2=''.join(sorted(t))
        return r1==r2
            
        
        
