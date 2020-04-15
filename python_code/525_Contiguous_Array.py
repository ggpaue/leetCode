#Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

#Example 1:
#Input: [0,1]
#Output: 2
#Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
#Example 2:
#Input: [0,1,0]
#Output: 2
#Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
#Note: The length of the given binary array will not exceed 50,000.

from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        tmp = {}
        tmp[0] = -1
        maxlen = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            if count in tmp:
                maxlen = max(maxlen, i - tmp[count])
            else:
                tmp[count] = i
        print(maxlen)
        return maxlen


s = Solution()
nums=[0,1,0,0,1,1,0]
s.findMaxLength(nums)