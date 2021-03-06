#Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.



#Example 1:

#Input: matrix =
#[
#  [0,1,1,1],
#  [1,1,1,1],
#  [0,1,1,1]
#]
#Output: 15
#Explanation:
#There are 10 squares of side 1.
#There are 4 squares of side 2.
#There is  1 square of side 3.
#Total number of squares = 10 + 4 + 1 = 15.
#Example 2:

#Input: matrix =
#[
#  [1,0,1],
#  [1,1,0],
#  [1,1,0]
#]
#Output: 7
#Explanation:
#There are 6 squares of side 1.
#There is 1 square of side 2.
#Total number of squares = 6 + 1 = 7.


#Constraints:

#1 <= arr.length <= 300
#1 <= arr[0].length <= 300
#0 <= arr[i][j] <= 1

from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix is None or len(matrix) == 0:
            return 0
        row = len(matrix)
        col = len(matrix[0])

        res = 0

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 1:
                    if r == 0 or c == 0:
                        res += 1
                    else:
                        tmp = min(matrix[r-1][c], matrix[r-1][c-1], matrix[r][c-1]) + matrix[r][c]
                        res += tmp
                        matrix[r][c] = tmp
        print(res)
        return res

matrix = [ [1,0,1], [1,1,0], [1,1,0]]
s = Solution()
s.countSquares(matrix)