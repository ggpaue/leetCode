#You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

#The area of an island is the number of cells with a value 1 in the island.

#Return the maximum area of an island in grid. If there is no island, return 0.



#Example 1:


#Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
#Output: 6
#Explanation: The answer is not 11, because the island must be connected 4-directionally.
#Example 2:

#Input: grid = [[0,0,0,0,0,0,0,0]]
#Output: 0


#Constraints:

#m == grid.length
#n == grid[i].length
#1 <= m, n <= 50
#grid[i][j] is either 0 or 1.

from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        m = len(grid[0])

        def traversal(i: int, j: int) -> int:
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + traversal(i-1, j) + traversal(i+1, j) + traversal(i, j-1) + traversal(i, j+1)

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    res = max(res, traversal(i, j))
        return res