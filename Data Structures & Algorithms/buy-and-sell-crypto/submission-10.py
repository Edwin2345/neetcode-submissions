class Solution:
    # buy on one day, sell on anotehr future day, can choose to not buy at all
    #brute force, calcualte profit for ebvery signle buy sell combno
    #O(N^2) time complexity as for each price check evry other future day
    #O(1) space
    def maxProfit(self, prices: List[int]) -> int:
        largestProfit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                largestProfit = max(largestProfit, prices[j] - prices[i])
        
        return largestProfit
        