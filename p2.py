<<<<<<< HEAD
#start
#https://leetcode.com/problems/palindrome-number/
=======
#https://leetcode.com/problems/palindrome-number
>>>>>>> 049aac22aac08949e056adbe56d1cb945f762627
#clink the above link to the problem description
class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        x=str(x)
        i=0
        i=int(i)
        j=int(len(x)/2)
        for i in range(j):
            if x[int(i)]!=x[int(len(x)-1-i)]:
                return False
        return True
        
#end
