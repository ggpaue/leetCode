#Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

#Return true if and only if we can do this in a way such that the resulting number is a power of 2.



#Example 1:

#Input: 1
#Output: true
#Example 2:

#Input: 10
#Output: false
#Example 3:

#Input: 16
#Output: true
#Example 4:

#Input: 24
#Output: false
#Example 5:

#Input: 46
#Output: true


#Note:

#1 <= N <= 10^9

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        res = sorted([int(x) for x in str(N)])
        print(res)
        for i in range(30):
            if sorted([int(x) for x in str(1<<i)]) == res:
                return True
        return False

s = Solution()
N = 16
s.reorderedPowerOf2(N)

print(1<<29)