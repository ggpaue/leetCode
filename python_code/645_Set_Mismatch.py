#You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

#You are given an integer array nums representing the data status of this set after the error.

#Find the number that occurs twice and the number that is missing and return them in the form of an array.



#Example 1:

#Input: nums = [1,2,2,4]
#Output: [2,3]
#Example 2:

#Input: nums = [1,1]
#Output: [1,2]


#Constraints:

#2 <= nums.length <= 104
#1 <= nums[i] <= 104

from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = [0] * (n+1)
        seen[0] = 1
        dup = -1
        for num in nums:
            if seen[num]:
                dup = num
            seen[num] = 1
        miss = -1
        for idx, num in enumerate(seen):
            if num == 0:
                if seen[idx] == 0:
                    miss = idx
        return [dup, miss]

s = Solution()
nums = [1,2,2,4]
s.findErrorNums(nums)