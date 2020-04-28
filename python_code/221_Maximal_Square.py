#Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

#Example:

#Input:

#1 0 1 0 0
#1 0 1 1 1
#1 1 1 1 1
#1 0 0 1 0

#Output: 4

from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * (n+1) for _ in range(m+1)]
        res = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j]) + 1
                    res = max(res, dp[i+1][j+1])
        print(res*res)
        return res * res


matrix = [['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']]
s = Solution()
s.maximalSquare(matrix)