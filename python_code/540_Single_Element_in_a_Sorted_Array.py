#You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.



#Example 1:

#Input: [1,1,2,3,3,4,4,8,8]
#Output: 2
#Example 2:

#Input: [3,3,7,7,10,11,11]
#Output: 10


#Note: Your solution should run in O(log n) time and O(1) space.

from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''
        res = 0
        for n in nums:
            res ^= n
        print(res)
        return res
        '''

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if (mid % 2 == 0 and nums[mid] == nums[mid+1]) or (mid % 2 != 0 and nums[mid] == nums[mid-1]):
                left = mid + 1
            else:
                right = mid
        print(nums[left])
        return nums[left]

nums = [1,1,2,3,3,4,4,8,8]
s = Solution()
s.singleNonDuplicate(nums)
