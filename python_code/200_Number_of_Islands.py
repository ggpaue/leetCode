#Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

#Example 1:

#Input:
#11110
#11010
#11000
#00000

#Output: 1
#Example 2:

#Input:
#11000
#11000
#00100
#00011

#Output: 3

from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) < 1:
            return 0

        row = len(grid)
        column = len(grid[0])
        res = 0

        def dfs(r, c):
            if r < 0 or r > row-1 or c < 0 or c > column-1 or grid[r][c] =='0':
                return

            grid[r][c]='0'

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for i in range(row):
            for j in range(column):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        print(res)
        return res


s = Solution()
grid = [['1','1','0','0','0'], ['1','1','0','0','0'], ['0','0','1','0','0'], ['0','0','0','1','1']]
s.numIslands(grid)