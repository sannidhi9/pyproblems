#https://leetcode.com/problems/palindrome-number/
#clink the above link to the problem description
class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        y,sum1=x,0
        if x<0:return False
        else:
            while y!=0:
                dig=y%10
                sum1=sum1*10+dig
                y=y//10
        if sum1==x:
            return True
        else:return False
