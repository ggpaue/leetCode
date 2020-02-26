#Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        j = 0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[j] = nums[i]
                j += 1
        nums[j] = nums[-1]
        j += 1
        return j


s = Solution()
nums=[0,0,1,1,1,2,2,3,3,4]
s.removeDuplicates(nums)