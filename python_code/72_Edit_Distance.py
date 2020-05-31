#Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

#You have the following 3 operations permitted on a word:

#Insert a character
#Delete a character
#Replace a character
#Example 1:

#Input: word1 = "horse", word2 = "ros"
#Output: 3
#Explanation:
#horse -> rorse (replace 'h' with 'r')
#rorse -> rose (remove 'r')
#rose -> ros (remove 'e')
#Example 2:

#Input: word1 = "intention", word2 = "execution"
#Output: 5
#Explanation:
#intention -> inention (remove 't')
#inention -> enention (replace 'i' with 'e')
#enention -> exention (replace 'n' with 'x')
#exention -> exection (replace 'n' with 'c')
#exection -> execution (insert 'u')

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = "!" + word1
        word2 = "!" + word2

        n1 = len(word1)
        n2 = len(word2)

        dp = [[0] * n2 for _ in range(n1)]

        for i in range(n1):
            dp[i][0] = i

        for j in range(n2):
            dp[0][j] = j

        for i in range(1, n1):
            for j in range(1, n2):
                cost = (word1[i] != word2[j])
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+cost)
        print(dp[-1][-1])
        return int(dp[-1][-1])

word1 = "horse"
word2 = "ros"

s = Solution()
s.minDistance(word1, word2)