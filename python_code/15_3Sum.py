#Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

#Notice that the solution set must not contain duplicate triplets.



#Example 1:

#Input: nums = [-1,0,1,2,-1,-4]
#Output: [[-1,-1,2],[-1,0,1]]
#Example 2:

#Input: nums = []
#Output: []
#Example 3:

#Input: nums = [0]
#Output: []


#Constraints:

#0 <= nums.length <= 3000
#-105 <= nums[i] <= 105

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return
        if len(nums) < 3:
            return []
        res = []
        nums.sort()
        i = 0
        while i < len(nums):
            tmps = self.twoSum(nums, i+1, -nums[i])
            for tmp in tmps:
                tmp.append(nums[i])
                res.append(tmp)
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return res



    def twoSum(self, nums: List[int], start: int, target: int) -> List[List[int]]:
        if nums is None:
            return
        if len(nums) == 0:
            return []

        res = []
        left, right = start, len(nums)-1
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
        return res

s = Solution()
nums = [-1,0,1,2,-1,-4]
s.threeSum(nums)

