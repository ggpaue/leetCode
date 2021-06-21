#Given an integer numRows, return the first numRows of Pascal's triangle.

#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




#Example 1:

#Input: numRows = 5
#Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#Example 2:

#Input: numRows = 1
#Output: [[1]]


#Constraints:

#1 <= numRows <= 30

from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        def helper(n):
            if n:
                helper(n-1)
                res.append([1]*n)
                for i in range(1, n-1):
                    res[n-1][i] = res[n-2][i] + res[n-2][i-1]
        helper(numRows)
        return res