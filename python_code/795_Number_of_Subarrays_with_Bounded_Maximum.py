#We are given an array nums of positive integers, and two positive integers left and right (left <= right).

#Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least left and at most right.

#Example:
#Input:
#nums = [2, 1, 4, 3]
#left = 2
#right = 3
#Output: 3
#Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
#Note:

#left, right, and nums[i] will be an integer in the range [0, 109].
#The length of nums will be in the range of [1, 50000].

from typing import List
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        i, j = 0, 0
        n = len(nums)

        cnt = 0
        res = 0

        while i <= j and j < n:
            if left <= nums[j] and nums[j] <= right:
                res += j-i+1
                cnt = j-i+1
            elif right < nums[j]:
                i = j + 1
                cnt = 0
            else:
                res += cnt
            j += 1
        return res