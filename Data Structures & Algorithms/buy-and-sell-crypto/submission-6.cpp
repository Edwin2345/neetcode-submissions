class Solution {
public:
    int maxProfit(vector<int>& prices) {
        //10,11,9,12
        int maxProfit = 0;
        int buyIndex = 0;
        for(int sellIndex=1; sellIndex<prices.size(); ++sellIndex){     
            //lower price in future, new possible max      
            if(prices[sellIndex] < prices[buyIndex]){
               buyIndex = sellIndex;
            }
            //profit possible -> update maxProfit
            else{
               int profit = prices[sellIndex] - prices[buyIndex];
               maxProfit = (profit > maxProfit) ? profit : maxProfit;
            }
        }

        return maxProfit;
    }
};
