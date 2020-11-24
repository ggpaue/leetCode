#Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

#Notice that the solution set must not contain duplicate quadruplets.



#Example 1:

#Input: nums = [1,0,-1,0,-2,2], target = 0
#Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#Example 2:

#Input: nums = [], target = 0
#Output: []

from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums: List[int], k: int, start: int, target: int):
            res = []
            if k < 2 or len(nums) < k:
                return res

            if k == 2:
                left, right = start, len(nums) - 1
                while left < right:
                    lo = nums[left]
                    hi = nums[right]
                    if lo + hi < target:
                        left += 1
                    elif lo + hi > target:
                        right -= 1
                    else:
                        res.append([lo, hi])
                        while left < right and nums[left] == lo:
                            left += 1
                        while left < right and nums[left] == hi:
                            hi -= 1
            else:
                i = start
                while i < len(nums):
                    tmps = kSum(nums, k-1, i+1, target-nums[i])
                    for tmp in tmps:
                        tmp.append(nums[i])
                        res.append(tmp)
                    while i < len(nums)-1 and nums[i] == nums[i+1]:
                        i += 1
                    i += 1
            return res

        nums.sort()
        return kSum(nums, 4, 0, 0)

s = Solution()
nums = [1,0,-1,0,-2,2]
s.fourSum(nums, 0)





