#Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

#Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

#Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

#Note:

#The order of returned grid coordinates does not matter.
#Both m and n are less than 150.


#Example:

#Given the following 5x5 matrix:

#  Pacific ~   ~   ~   ~   ~
#       ~  1   2   2   3  (5) *
#       ~  3   2   3  (4) (4) *
#       ~  2   4  (5)  3   1  *
#       ~ (6) (7)  1   4   5  *
#       ~ (5)  1   1   2   4  *
#          *   *   *   *   * Atlantic

#Return:

#[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

from typing import List
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])

        p_visited = set()
        a_visited = set()

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(visited, x, y):
            visited.add((x, y))
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and matrix[nx][ny] >= matrix[x][y]:
                    dfs(visited, nx, ny)

        for i in range(m):
            dfs(p_visited, i, 0)
            dfs(a_visited, i, n-1)

        for j in range(n):
            dfs(p_visited, 0, j)
            dfs(a_visited, m-1, j)

        return list(p_visited.intersection(a_visited))