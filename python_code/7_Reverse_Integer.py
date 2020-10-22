#Given a 32-bit signed integer, reverse digits of an integer.

#Note:
#Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.



#Example 1:

#Input: x = 123
#Output: 321
#Example 2:

#Input: x = -123
#Output: -321
#Example 3:

#Input: x = 120
#Output: 21
#Example 4:

#Input: x = 0
#Output: 0


#Constraints:

#-231 <= x <= 231 - 1

class Solution:
    def reverse(self, x: int) -> int:
        res = 0

        if x < 0:
            sig = -1
            x *= -1
        else:
            sig = 1

        while x > 0:
            tmp = x % 10
            res = res * 10 + tmp
            x = int(x / 10)

        if res * sig >= 2 ** 31 - 1 or res * sig <= -2 ** 31:
            return 0
        return res * sig

s = Solution()
x=-123
s.reverse(x)