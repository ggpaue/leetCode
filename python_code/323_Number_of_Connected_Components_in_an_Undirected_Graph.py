#You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

#Return the number of connected components in the graph.



#Example 1:


#Input: n = 5, edges = [[0,1],[1,2],[3,4]]
#Output: 2
#Example 2:


#Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
#Output: 1


#Constraints:

#1 <= n <= 2000
#1 <= edges.length <= 5000
#edges[i].length == 2
#0 <= ai <= bi < n
#ai != bi
#There are no repeated edges.

from typing import List
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n <= 1:
            return n
        res = 0
        adj_list = defaultdict(list)

        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        seen_nodes = set()

        def search_neighbors(node):
            seen_nodes.add(node)
            for curr in adj_list[node]:
                if curr not in seen_nodes:
                    search_neighbors(curr)

        for num in range(n):
            if num not in seen_nodes:
                search_neighbors(num)
                res += 1
        return res