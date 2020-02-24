#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Example:

#Given nums = [2, 7, 11, 15], target = 9,

#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp = {}
        res = []
        i = 0
        for i in range(len(nums)):
            if target - nums[i] in tmp:
                res = [tmp.get(target - nums[i]), i]
                break
            tmp[nums[i]] = i
            i += 1
        return res



s = Solution()
nums = [2, 7, 11, 15]
target = 9
s.twoSum(nums, target)