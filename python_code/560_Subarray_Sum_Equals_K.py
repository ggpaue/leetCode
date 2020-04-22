#Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

#xample 1:
#Input:nums = [1,1,1], k = 2
#Output: 2
#Note:
#The length of the array is in range [1, 20,000].
#The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

from typing import List
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        tmp = defaultdict(int)
        sum = 0
        res = 0

        for n in nums:
            sum += n
            if sum == k:
                res += 1
            elif sum - k in tmp:
                res += tmp[sum - k]
            tmp[sum] += 1
        return res

s = Solution()
nums = [1,1,1]
k = 2
s.subarraySum(nums, k)