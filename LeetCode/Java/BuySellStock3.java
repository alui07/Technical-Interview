/* 123. Best Time to Buy and Sell Stock III
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
*/
class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length == 0) return 0;
        int buy = prices[0];
        int maxProfit = 0;
        int numTransactions = 0;
        int lowestProfit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] < prices[i-1]) {
                System.out.println("sell, i:"+i+":"+prices[i]+", trans:"+numTransactions);
                int profit = prices[i-1] - buy;
                if(numTransactions == 0 && i==1) {
                    buy = prices[i];
                } else if (numTransactions < 2) {
                    maxProfit += profit;
                    buy = prices[i];
                    if (numTransactions == 0) {
                        lowestProfit = maxProfit;
                    } else if (profit < lowestProfit) {
                        lowestProfit = profit;
                    }
                    numTransactions++;
                } else if (numTransactions >= 2 && profit > lowestProfit){
                    int tempLowestProfit = 0;
                    if (profit > (maxProfit + 1) / 2) {
                        tempLowestProfit = maxProfit - lowestProfit;
                    } else {
                        tempLowestProfit = profit;
                    }
                    maxProfit += profit - lowestProfit;
                    buy = prices[i];
                    lowestProfit = tempLowestProfit;
                }
            } else if (i == prices.length-1 && prices[i] > buy) {
                int profit = prices[i] - buy;
                if (numTransactions < 2) {
                    maxProfit += profit;
                } else if (profit > lowestProfit) {
                    maxProfit += profit-lowestProfit;
                }
            }
        }
        return maxProfit;
    }
}