#You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

#What is the maximum number of envelopes can you Russian doll? (put one inside other)

#Note:
#Rotation is not allowed.

#Example:

#Input: [[5,4],[6,4],[6,7],[2,3]]
#Output: 3
#Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

from typing import List
import bisect
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if len(envelopes) == 0:
            return 0

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        def lis(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect.bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)

        return lis([i[1] for i in envelopes])


s = Solution()
envelops = [[5,4],[6,4],[6,7],[2,3]]
s.maxEnvelopes(envelops)