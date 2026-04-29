class Solution {
public:
    int maxProfit(vector<int>& prices) {
        //10,11,9,12
        int maxProfit = 0;
        int L = 0;
        for(int R=1; R<prices.size(); ++R){     
            //profit possible -> set max      
            if(prices[R] > prices[L]){
                int profit = prices[R] - prices[L];
                maxProfit = (profit > maxProfit) ? profit : maxProfit;
            }
            //lower price found, set as new buy
            else{
                L = R;
            }
        }

        return maxProfit;
    }
};
