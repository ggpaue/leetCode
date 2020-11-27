#Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

#Example 1:
#Input: "sea", "eat"
#Output: 2
#Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
#Note:
#The length of given words won't exceed 500.
#Characters in given words can only be lower-case letters.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if m == 0:
            return n
        if n == 0:
            return m
        lcs = self.longestCommonSubsequence(word1, word2)
        return m - lcs + n - lcs

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = ' ' + text1
        text2 = ' ' + text2

        dp = [[0 for i in range(len(text2))] for j in range(len(text1)) ]

        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]


