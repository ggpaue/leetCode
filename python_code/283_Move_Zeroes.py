#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#Example:

#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]
#Note:

#You must do this in-place without making a copy of the array.
#Minimize the total number of operations.

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return
        z_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[z_pos], nums[i] = nums[i], nums[z_pos]
                z_pos += 1
        print(nums)

s = Solution()
nums=[0,1,0,3,12]
s.moveZeroes(nums)