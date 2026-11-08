class Solution:
    # buy on one day, sell on anotehr future day, can choose to not buy at all
    #optimizatiuon: if future sell day price is lower than current buy day, we should
    #actually buy on that day and look for future sell day
    #use 2 pointers, buyDay, sellDay and slide them across an increasing window
    #O(N) time as single pass, O(1) space
    def maxProfit(self, prices: List[int]) -> int:
        largestProfit = 0
        buyDay = 0
        for sellDay in range(1, len(prices)): 
            #if profit possible calualte it
            if prices[buyDay] < prices[sellDay]:
               largestProfit = max(largestProfit, prices[sellDay] - prices[buyDay])
            #otherwise, we should acutally buy at thsi lower price adn look for future sell
            else: 
               buyDay = sellDay

        
        return largestProfit
        