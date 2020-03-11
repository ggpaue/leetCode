#Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

#Your algorithm's runtime complexity must be in the order of O(log n).

#If the target is not found in the array, return [-1, -1].

#Example 1:

#Input: nums = [5,7,7,8,8,10], target = 8
#Output: [3,4]
#Example 2:

#Input: nums = [5,7,7,8,8,10], target = 6
#Output: [-1,-1]

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                # found the target, now find the range
                for i in range(left, right+1):
                    if nums[i] == target:
                        if left < i and nums[left] != nums[i]:
                            left = i
                        right = i
                return [left, right]
        return [-1, -1]