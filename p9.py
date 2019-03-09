
#https://leetcode.com/problems/plus-one/
#visit the above link to see problem description
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=len(digits)-1
        if x>=0:
            digits[x]=digits[x]+1
            for i in range(x,-1,-1):
                if digits[i]>9 and i>0:
                    digits[i]=0
                    digits[i-1]=digits[i-1]+1
                elif digits[i]>9 and i==0:
                    digits[i]=0
                    digits=[1]+digits
            return digits
        else:
            return [1]
