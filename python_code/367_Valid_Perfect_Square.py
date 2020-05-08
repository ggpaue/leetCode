#Given a positive integer num, write a function which returns True if num is a perfect square else False.

#Note: Do not use any built-in library function such as sqrt.

#Example 1:

#Input: 16
#Output: true
#Example 2:

#Input: 14
#Output: false

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l = 0
        r = num // 2
        def helper(l, r, num):
            while l < r:
                mid = (l + r) // 2
                if mid * mid == num:
                    return True
                elif mid * mid < num:
                    return helper(mid+1, r, num)
                else:
                    return helper(l, mid-1, num)
            return False
        return helper(l, r, num)

s = Solution()
s.isPerfectSquare(num=16)