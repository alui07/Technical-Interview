""" 322. Coin Change
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins) == 0: return -1
        if amount == 0: return 0
        coinChanges, minCoins = [], [0]
        for coin in range(len(coins)):
            coinChanges.append([0])
        for i in range(1,amount+1):
            minCoins.append(i)
            foundValidCoin = False
            for coin in range(len(coinChanges)):
                difference = i - coins[coin]
                #print("difference", i, coins[coin])
                if (difference > -1):
                    numCoins = minCoins[difference] + 1
                    if numCoins == 0:
                        if coins[coin] != i:
                            # print("broke")
                            # print(coinChanges)
                            # print(minCoins)
                            coinChanges[coin].append(-1)
                            if not foundValidCoin: minCoins[i] = -1
                            continue
                    
                    foundValidCoin = True
                    coinChanges[coin].append(numCoins)
                    if minCoins[i] > numCoins or minCoins[i] == -1: minCoins[i] = numCoins
                else:
                    coinChanges[coin].append(-1)
                    if not foundValidCoin: minCoins[i] = -1
                #print(coinChanges)
                #print(minCoins)
        return minCoins[len(minCoins)-1] or -1