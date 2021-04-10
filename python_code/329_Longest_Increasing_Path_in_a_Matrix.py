#Given an m x n integers matrix, return the length of the longest increasing path in matrix.

#From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).



#Example 1:


#Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
#Output: 4
#Explanation: The longest increasing path is [1, 2, 6, 9].
#Example 2:


#Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
#Output: 4
#Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
#Example 3:

#Input: matrix = [[1]]
#Output: 1


#Constraints:

#m == matrix.length
#n == matrix[i].length
#1 <= m, n <= 200
#0 <= matrix[i][j] <= 231 - 1

from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        visited = {}
        def dfs(row, col):
            path = 0
            for nrow, ncol in (row+1, col), (row-1, col), (row, col+1), (row, col-1):
                if 0 <= nrow <= len(matrix)-1 and 0 <= ncol <= len(matrix[0])-1 and matrix[nrow][ncol] > matrix[row][col]:
                    if (nrow, ncol) in visited:
                        path = max(path, visited[(nrow, ncol)])
                    else:
                        path = max(path, dfs(nrow, ncol))
            visited[(row, col)] = path + 1
            return path + 1

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if (r, c) not in visited:
                    dfs(r, c)

        return max(visited.values())