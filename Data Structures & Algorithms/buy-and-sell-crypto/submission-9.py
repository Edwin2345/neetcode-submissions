class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        largestProfit = 0
        buyDay = 0
        for sellDay in range(1, len(prices)):
            #if cheaper to buy on sellDay, that should be buyDay
            if prices[buyDay] > prices[sellDay]:
               buyDay = sellDay
            #otehwrise, calc profit and update amx
            else:
               largestProfit = max(largestProfit, prices[sellDay]- prices[buyDay]) 

        return largestProfit 
        