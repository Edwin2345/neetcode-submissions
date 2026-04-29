public class Solution {
    public int MaxProfit(int[] prices) {
        int buyDay=0;
        int maxProfit=0;
        for(int sellDay=1; sellDay<prices.Length; ++sellDay){
            if(prices[buyDay] > prices[sellDay]){
                buyDay = sellDay;
            }
            else if(prices[sellDay]-prices[buyDay] > maxProfit){
                maxProfit = prices[sellDay]-prices[buyDay];
            }
        }

        return maxProfit;
    }
}
