#Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.



#Example 1:

#Input: s1 = "ab" s2 = "eidbaooo"
#Output: True
#Explanation: s2 contains one permutation of s1 ("ba").
#Example 2:

#Input:s1= "ab" s2 = "eidboaoo"
#Output: False


#Note:

#The input strings only contain lower case letters.
#The length of both given strings is in range [1, 10,000].

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counter = Counter(s1)
        s2Counter = Counter(s2[:len(s1)-1])

        for i in range(len(s1)-1, len(s2)):
            start = i - len(s1) + 1
            s2Counter[s2[i]] += 1

            if s1Counter == s2Counter:
                return True
            s2Counter[s2[start]] -= 1

            if s2Counter[s2[start]] == 0:
                del s2Counter[s2[start]]

        return False

s1= "ab"
s2 = "eidbaooo"
print(s2[:1])

tmp1 = Counter({'i': 1, 'd': 1, 'e': 0})
tmp2 = Counter({'i': 1, 'd': 1})

s = Solution()
s.checkInclusion(s1, s2)