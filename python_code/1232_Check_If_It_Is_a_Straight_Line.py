#You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

#Example 1:

#Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
#Output: true

#Example 2:

#Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
#Output: false

from typing import List
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        try:
            slope = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        except:
            slope = None
        for i in range(2, len(coordinates)):
            try:
                tmp = (coordinates[i][1] - coordinates[0][1]) / (coordinates[i][0] - coordinates[0][0])
            except:
                tmp = None
            if tmp != slope:
                return False
        return True