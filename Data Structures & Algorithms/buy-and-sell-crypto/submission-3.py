class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0;
        
        L = 0
        maxProfit = 0
        for R in range(1,len(prices)):
            #found a lower price
            if(prices[R] < prices[L]):
                L = R
            #else if profit possible, set max
            elif(prices[R] > prices[L]):
                maxProfit = max(prices[R] - prices[L], maxProfit)

        return maxProfit
        