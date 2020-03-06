#We are playing the Guess Game. The game is as follows:

#I pick a number from 1 to n. You have to guess which number I picked.

#Every time you guess wrong, I'll tell you whether the number is higher or lower.

#You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

#-1 : My number is lower
# 1 : My number is higher
# 0 : Congrats! You got it!
#Example :

#Input: n = 10, pick = 6
#Output: 6

class Solution(object):
    def guess(self, n):
        target = 6
        if n == target:
            return 0
        elif n > target:
            return -1
        else:
            return 1

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low <= high:
            mid = (low+high)//2
            if self.guess(mid) == 0:
                print(mid)
                return mid
            elif self.guess(mid) == -1:
                high = mid - 1
            else:
                low = mid + 1
        return None

s = Solution()
n = 10
s.guessNumber(n)
