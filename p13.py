#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#visit the above link to see problem definition
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:return 0
        temp,r=prices[len(prices)-1],0
        for i in range(len(prices)-1,-1,-1):
            temp=max(temp,prices[i])
            if temp-prices[i]>r:
                r=temp-prices[i]
        return r 
