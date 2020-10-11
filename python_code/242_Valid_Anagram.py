#Given two strings s and t , write a function to determine if t is an anagram of s.

#Example 1:

#Input: s = "anagram", t = "nagaram"
#Output: true
#Example 2:

#Input: s = "rat", t = "car"
#Output: false
#Note:
#You may assume the string contains only lowercase alphabets.

#Follow up:
#What if the inputs contain unicode characters? How would you adapt your solution to such case?

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        tmp = dict()

        for n in s:
            if n in tmp:
                tmp[n] += 1
            else:
                tmp[n] = 1

        for m in t:
            if m in tmp:
                tmp[m] -= 1
            else:
                return False

        for c in tmp:
            if tmp[c] != 0:
                return False
        return True

s1 = Solution()
s = "anagram"
t = "nagaram"
s1.isAnagram(s, t)