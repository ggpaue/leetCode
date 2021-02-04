#Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.



#Example 1:

#Input: a = 2, b = [3]
#Output: 8
#Example 2:

#Input: a = 2, b = [1,0]
#Output: 1024
#Example 3:

#Input: a = 1, b = [4,3,3,8,5,2]
#Output: 1
#Example 4:

#Input: a = 2147483647, b = [2,0,0]
#Output: 1198


#Constraints:

#1 <= a <= 231 - 1
#1 <= b.length <= 2000
#0 <= b[i] <= 9
#b doesn't contain leading zeros.

from typing import List
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        base = 1337
        def mypow(a, k):
            if k == 0:
                return 1
            a %= base
            if k % 2 == 1:
                return (a * mypow(a, k-1)) % base
            else:
                sub = mypow(a, k/2)
                return (sub*sub) % base
        if len(b) == 0:
            return 1
        last = b.pop()

        part1 = mypow(a, last)
        part2 = mypow(self.superPow(a, b), 10)
        return (part1 * part2) % base
