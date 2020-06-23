#Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

#Note:

#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

#Example 1:

#Input: [2,2,3,2]
#Output: 3
#Example 2:

#Input: [0,1,0,1,0,1,99]
#Output: 99

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for i in range(32):
            count = 0
            for num in nums:
                if num & (1 << i) == (1 << i):
                    count += 1
                single |= (count % 3) << i

        return single if single < (1 << 31) else single - (1 << 32)