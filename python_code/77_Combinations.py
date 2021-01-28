#Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

#You may return the answer in any order.



#Example 1:

#Input: n = 4, k = 2
#Output:
#[
#  [2,4],
#  [3,4],
#  [2,3],
#  [1,2],
#  [1,3],
#  [1,4],
#]
#Example 2:

#Input: n = 1, k = 1
#Output: [[1]]


#Constraints:

#1 <= n <= 20
#1 <= k <= n

from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(n, k, start, tmp):
            if k == len(tmp):
                res.append(tmp[:])
            for i in range(start, n+1):
                tmp.append(i)
                backtrack(n, k, i+1, tmp)
                tmp.pop()
        backtrack(n, k, 1, [])
        return res
