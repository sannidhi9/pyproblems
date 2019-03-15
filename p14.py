#https://leetcode.com/problems/valid-palindrome/
#visit the above link to see description
class Solution:
    def isPalindrome(self, s: 'str') -> 'bool':
        a,j="",0
        for i in range(len(s)):
            if s[i].isalpha()==True:
                a=a+s[i].lower()
            elif s[i].isnumeric()==True:
                a=a+str(s[i])
        r=a[::-1]
        return r==a
