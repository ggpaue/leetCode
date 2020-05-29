#There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

#Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

#Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



#Example 1:

#Input: numCourses = 2, prerequisites = [[1,0]]
#Output: true
#Explanation: There are a total of 2 courses to take.
#             To take course 1 you should have finished course 0. So it is possible.
#Example 2:

#Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
#Output: false
#Explanation: There are a total of 2 courses to take.
#             To take course 1 you should have finished course 0, and to take course 0 you should
#             also have finished course 1. So it is impossible.


#Constraints:

#The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
#You may assume that there are no duplicate edges in the input prerequisites.
#1 <= numCourses <= 10^5

from typing import List
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.adj_dict = defaultdict(set)

        for i, j in prerequisites:
            self.adj_dict[i].add(j)

        self.visited = [0] * numCourses
        self.foundCycle = 0

        for i in range(numCourses):
            if self.foundCycle == 1:
                break
            if self.visited[i] == 0:
                self.dfs(i)
        return self.foundCycle == 1

    def dfs(self, start):
        if self.foundCycle == 1:
            return

        if self.visited[start] == 1:
            self.foundCycle = 1

        if self.visited[start] == 0:
            self.visited[start] = 1
            for n in self.adj_dict[start]:
                self.dfs(n)
            self.visited[start] = 2
