#Say you have an array for which the ith element is the price of a given stock on day i.

#Design an algorithm to find the maximum profit. You may complete at most two transactions.

#Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).



#Example 1:

#Input: prices = [3,3,5,0,0,3,1,4]
#Output: 6
#Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
#Example 2:

#Input: prices = [1,2,3,4,5]
#Output: 4
#Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
#Example 3:

#Input: prices = [7,6,4,3,1]
#Output: 0
#Explanation: In this case, no transaction is done, i.e. max profit = 0.
#Example 4:

#Input: prices = [1]
#Output: 0


#Constraints:

#1 <= prices.length <= 105
#0 <= prices[i] <= 105

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''

        :param prices:
        :return:

        dp_i10 = 0
        dp_i11 = -prices[0]
        dp_i20 = 0
        dp_i21 = -prices[0]

        for i in range(len(prices)):
            dp_i20 = max(dp_i20, dp_i21 + prices[i])
            dp_i21 = max(dp_i21, dp_i10 - prices[i])
            dp_i10 = max(dp_i10, dp_i11 + prices[i])
            dp_i11 = max(dp_i11, -prices[i])
        return dp_i20
        '''

        dp = [[[0 for x in range(2)] for y in range(1, 3)] for z in range(len(prices))]
        dp[0][1][0] = 0
        dp[0][1][1] = -prices[0]
        dp[0][2][0] = 0
        dp[0][2][1] = -prices[0]

        for i in range(1, len(prices)):
            for k in reversed(range(1, 3)):
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        return dp[len(prices)-1][2][0]