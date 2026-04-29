class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        maxProfit = 0
        for sell in range(1,len(prices)):
            if prices[buy] > prices[sell]:
                buy = sell
            maxProfit = max(maxProfit, prices[sell] - prices[buy])

        return maxProfit