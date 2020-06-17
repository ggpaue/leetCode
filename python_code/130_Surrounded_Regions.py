#Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

#A region is captured by flipping all 'O's into 'X's in that surrounded region.

#Example:

#X X X X
#X O O X
#X X O X
#X O X X
#After running your function, the board should be:

#X X X X
#X X X X
#X X X X
#X O X X
#Explanation:

#Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

from typing import List
class Solution:
    def dfs(self, i, j):
        if i < 0 or j < 0 or i >= self.m or j >= self.n or self.board[i][j] != 'O':
            return

        self.board[i][j] = 'T'
        neighbor = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
        for x, y in neighbor:
            self.dfs(x, y)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 0

        self.board = board
        self.m = len(board)
        self.n = len(board[0])

        for i in range(self.m):
            self.dfs(i, 0)
            self.dfs(i, self.n-1)

        for j in range(self.n):
            self.dfs(0, j)
            self.dfs(self.m-1, j)

        for i in range(self.m):
            for j in range(self.n):
                board[i][j] = "X" if board[i][j] != "T" else "O"



