#Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.



#Example 1:

#Input: nums = [1,5,11,5]
#Output: true
#Explanation: The array can be partitioned as [1, 5, 5] and [11].
#Example 2:

#Input: nums = [1,2,3,5]
#Output: false
#Explanation: The array cannot be partitioned into equal sum subsets.


#Constraints:

#1 <= nums.length <= 200
#1 <= nums[i] <= 100

from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return True
        sum = 0
        for num in nums:
            sum += num
        if sum % 2 != 0:
            return False

        sum = sum//2

        dp = [[0 for i in range(sum+1)] for _ in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0] = 1

        for i in range(1, len(nums)+1):
            for j in range(1, sum+1):
                if j - nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i-1]]
        return dp[len(nums)][sum]


s = Solution()
nums=[1,2,3,5]
s.canPartition(nums)
