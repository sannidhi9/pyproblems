#https://leetcode.com/problems/factorial-trailing-zeroes/
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0
        fact=str(math.factorial(n))
        for i in range(len(fact)-1,-1,-1):
            if fact[i]!='0':
                return count
            count=count+1
        return count
        
