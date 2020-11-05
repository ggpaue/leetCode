#Given a collection of distinct integers, return all possible permutations.

#Example:

#Input: [1,2,3]
#Output:
#[
#  [1,2,3],
#  [1,3,2],
#  [2,1,3],
#  [2,3,1],
#  [3,1,2],
#  [3,2,1]
#]

from typing import List
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 0:
            return res

        self.get_permute(res, nums, 0)
        print(res)
        return res

    def get_permute(self, res, nums, index):
        if index == len(nums):
            res.append(list(nums))
            return

        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self.get_permute(res, nums, index+1)
            nums[i], nums[index] = nums[index], nums[i]
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index=0):
            if index == len(nums):
                res.append(nums[:])

            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                backtrack(index+1)
                nums[i], nums[index] = nums[index], nums[i]

        backtrack()
        print(res)
        return res


tmp = [1,2,3]
s = Solution()
s.permute(tmp)