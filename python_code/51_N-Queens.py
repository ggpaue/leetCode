#The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



#Given an integer n, return all distinct solutions to the n-queens puzzle.

#Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

#Example:

#Input: 4
#Output: [
# [".Q..",  // Solution 1
#  "...Q",
#  "Q...",
#  "..Q."],

# ["..Q.",  // Solution 2
#  "Q...",
#  "...Q",
#  ".Q.."]
#]
#Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = set()
        res = []
        cols = [0] * n
        hill_diagonals = [0] * (2*n-1)
        dale_diagnoals = [0] * (2*n-1)

        def could_place(row, col):
            return not (cols[col] + hill_diagonals[row-col] + dale_diagnoals[row+col])

        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            hill_diagonals[row-col] = 1
            dale_diagnoals[row+col] = 1

        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            hill_diagonals[row-col] = 0
            dale_diagnoals[row+col] = 0

        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n-col-1))
            res.append(solution)

        def backtrack(row=0):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row == n-1:
                        add_solution()
                    else:
                        backtrack(row+1)
                    remove_queen(row, col)

        backtrack()
        return res