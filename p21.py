#https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        i,r,s,t=0,0,str(n),[]
        while(i<len(s)):
            r+=int(s[i])**2
            i+=1
            if i==len(s):
                if r==1:return True
                elif r in set(t):return False
                t.append(r)
                s,i,r=str(r),0,0
