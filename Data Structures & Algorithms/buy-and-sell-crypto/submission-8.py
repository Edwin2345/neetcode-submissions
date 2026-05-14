class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        largestProfit = 0
        buyDay = 0
        sellDay = 1

        while sellDay < len(prices):
              #if the sell day price is cheaper than buy, choose to buy on that day instead
              if prices[buyDay] > prices[sellDay]:
                 buyDay = sellDay
              #otherwise, calulate profit adn update max
              else:
                  largestProfit = max(largestProfit, prices[sellDay] - prices[buyDay])
              #go to next sell day
              sellDay += 1

        return largestProfit