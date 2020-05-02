#You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

#The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

#Example 1:

#Input: J = "aA", S = "aAAbbbb"
#Output: 3
#Example 2:

#Input: J = "z", S = "ZZ"
#Output: 0
#Note:

#S and J will consist of letters and have length at most 50.
#The characters in J are distinct.

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if J is None or S is None:
            return 0

        stone_set = set()
        res = 0
        for ch in J:
            stone_set.add(ch)

        for ch in S:
            if ch in stone_set:
                res += 1
        return res

J="aA"
S="aAAbbbb"
s=Solution()
s.numJewelsInStones(J, S)