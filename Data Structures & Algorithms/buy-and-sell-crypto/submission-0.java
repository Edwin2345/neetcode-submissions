class Solution {
    public int maxProfit(int[] prices) {
        int buyPtr=0;
        int profit=0;
        for(int sellPtr=1; sellPtr<prices.length; ++sellPtr){
            //next day lower -> move buyPtr ther
            if(prices[buyPtr] > prices[sellPtr]){
                buyPtr = sellPtr;
            }
            //next day higher -> sell and see if max
            else if(profit < prices[sellPtr] - prices[buyPtr]){
                profit = prices[sellPtr] - prices[buyPtr]; 
            }
        }


        return profit;
    }
}
