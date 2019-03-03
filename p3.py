#start
#https://leetcode.com/problems/roman-to-integer/
#clink on above link to see problem definition 
class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        r="IVXLCDM00"
        j=int(len(s))
        sum=0
        sum=int(sum)
        k=0
        k=int(k)
        for k in range(j):
            sum=sum+int(roman[str(s[k])])
            i=0
            if k>=1:
                
                for i in range(len(r)):
                        
                        if s[k]==r[i] and (s[k-1]==r[i-1] or s[k-1]==r[i-2]):
                            sum=sum-2*int(roman[str(s[k-1])])
        return sum
            
#end     
