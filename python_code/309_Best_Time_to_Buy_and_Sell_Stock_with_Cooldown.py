#Say you have an array for which the ith element is the price of a given stock on day i.

#Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

#You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
#Example:

#Input: [1,2,3,0,2]
#Output: 3
#Explanation: transactions = [buy, sell, cooldown, buy, sell]

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        dp = [[0 for x in range(2)] for y in range(len(prices))]

        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        return dp[len(prices)][0]