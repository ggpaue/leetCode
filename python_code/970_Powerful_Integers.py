#Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.

#An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.

#You may return the answer in any order. In your answer, each value should occur at most once.



#Example 1:

#Input: x = 2, y = 3, bound = 10
#Output: [2,3,4,5,7,9,10]
#Explanation:
#2 = 20 + 30
#3 = 21 + 30
#4 = 20 + 31
#5 = 21 + 31
#7 = 22 + 31
#9 = 23 + 30
#10 = 20 + 32
#Example 2:

#Input: x = 3, y = 5, bound = 15
#Output: [2,4,6,8,10,14]


#Constraints:

#1 <= x, y <= 100
#0 <= bound <= 106

from typing import List
from math import log
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        '''

        :param x:
        :param y:
        :param bound:
        :return:

        res = set()
        xi = 1
        while xi < bound:
            yj = 1
            while xi + yj <= bound:
                res.add(xi+yj)
                if y == 1:
                    break
                yj *= y
            if x == 1:
                break
            xi *= x
        return list(res)
        '''

        res = set()
        for i in range(int(log(bound, x))+1 if x != 1 else 1):
            for j in range(int(log(bound, y))+1 if y != 1 else 1):
                num = x ** i + y ** j
                if num <= bound:
                    res.add(num)
                else:
                    break
        return list(res)
