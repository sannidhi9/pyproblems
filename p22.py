#https://leetcode.com/problems/count-primes/
class Solution:
    def countPrimes(self, n: int) -> int:
        count=0
        if n<2:
            return 0
        prime = [True for i in range(n+1)] 
        p = 2
        while (p * p <= n): 
            if (prime[p] == True): 
                for i in range(p * 2, n+1, p): 
                    prime[i] = False
            p += 1
        for p in range(2, n): 
            if prime[p]: 
                count=count+1
        return count
    
