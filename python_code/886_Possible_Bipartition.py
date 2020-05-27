#Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

#Each person may dislike some other people, and they should not go into the same group.

#Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

#Return true if and only if it is possible to split everyone into two groups in this way.



#Example 1:

#Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
#Output: true
#Explanation: group1 [1,4], group2 [2,3]
#Example 2:

#Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
#Output: false
#Example 3:

#Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
#Output: false


#Note:

#1 <= N <= 2000
#0 <= dislikes.length <= 10000
#1 <= dislikes[i][j] <= N
#dislikes[i][0] < dislikes[i][1]
#There does not exist i != j for which dislikes[i] == dislikes[j].

from typing import List
import collections
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def helper(id, color):
            color_table[id] = color
            for other in dislike_table[id]:
                if color_table[other] == color:
                    return False

                if color_table[other] == 0 and (not helper(other, -color)):
                    return False
            return True

        if N <= 1 or not dislikes:
            return True

        dislike_table = collections.defaultdict(list)
        color_table = [0 for _ in range(N+1)]

        for p1, p2 in dislikes:
            dislike_table[p1].append(p2)
            dislike_table[p2].append(p1)

        for id in range(1, N+1):
            if color_table[id] == 0 and (not helper(id, 1)):
                return False
        return True


