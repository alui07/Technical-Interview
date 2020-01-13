""" 121. Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

#52 ms/98.61,13.8MB/90.80%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxProfit is self explanatory, maxSell is the highest price in the
        # list (which you would sell at)
        maxProfit, maxSell = 0, 0
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > maxSell: maxSell = prices[i]
            elif maxSell - prices[i] > maxProfit: maxProfit = maxSell - prices[i]
        return maxProfit

#60ms/81.72, 13.7MB/98.85%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        maxProfit, minBuy = 0, prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minBuy: minBuy = prices[i]
            elif prices[i] - minBuy > maxProfit: maxProfit = prices[i]-minBuy
        return maxProfit