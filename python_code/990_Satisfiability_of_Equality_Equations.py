#Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

#Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.



#Example 1:

#Input: ["a==b","b!=a"]
#Output: false
#Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.
#Example 2:

#Input: ["b==a","a==b"]
#Output: true
#Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
#Example 3:

#Input: ["a==b","b==c","a==c"]
#Output: true
#Example 4:

#Input: ["a==b","b!=c","c==a"]
#Output: false
#Example 5:

#Input: ["c==c","b==d","x!=z"]
#Output: true


#Note:

#1 <= equations.length <= 500
#equations[i].length == 4
#equations[i][0] and equations[i][3] are lowercase letters
#equations[i][1] is either '=' or '!'
#equations[i][2] is '='

from typing import List
import collections
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = collections.defaultdict(list)
        nonmatch = set()

        for eq in equations:
            v1 = eq[0]
            v2 = eq[-1]

            sign = eq[1:3]

            if sign == '==':
                graph[v1].append(v2)
                graph[v2].append(v1)
            else:
                nonmatch.add((v1, v2))

        parent = dict()

        def find(x):
            parent.setdefault(x,x)
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                parent[px] = py

        for key, val in graph.items():
            px = find(key)
            for y in val:
                py = find(y)
                if px != py:
                    union(key, y)

        for x, y in nonmatch:
            px = find(x)
            py = find(y)

            if px == py:
                return False
        return True
