#Given a collection of intervals, merge all overlapping intervals.

#Example 1:

#Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#Example 2:

#Input: intervals = [[1,4],[4,5]]
#Output: [[1,5]]
#Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.



#Constraints:

#intervals[i][0] <= intervals[i][1]

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''

        :param intervals:
        :return:
                if intervals is None:
            return

        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        pos = 0

        while pos < len(intervals) - 1:
            if intervals[pos][1] >= intervals[pos+1][0]:
                next = intervals.pop(pos+1)
                if next[1] > intervals[pos][1]:
                    intervals[pos][1] = next[1]
            else:
                pos += 1
        return intervals
        '''

        if intervals is None:
            return

        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            cur = intervals[i]
            last = res[-1]

            if cur[0] <= last[1]:
                last[1] = max(last[1], cur[1])
            else:
                res.append(cur)
        return res







test = [[1,3],[2,6],[8,10],[15,18]]
s = Solution()
s.merge(test)
