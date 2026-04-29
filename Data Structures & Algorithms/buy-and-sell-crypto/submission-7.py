class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyIndex = 0
        maxProfit = 0
        for sellIndex in range(len(prices)):
            #if sell is higher than buy, profit possible -> update maxProfit
            if prices[sellIndex] - prices[buyIndex] > maxProfit:
               maxProfit = prices[sellIndex] - prices[buyIndex]                                           
            #else if sell is lower than buy, new buy pointer
            elif prices[sellIndex] < prices[buyIndex]:
               buyIndex = sellIndex 
        
        return maxProfit