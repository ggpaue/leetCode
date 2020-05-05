#Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

#Examples:

#s = "leetcode"
#return 0.

#s = "loveleetcode",
#return 2.
#Note: You may assume the string contain only lowercase letters.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not str:
            return -1

        tmp = {}
        for ch in s:
            if ch in tmp:
                tmp[ch] += 1
            else:
                tmp[ch] = 1
        for i, ch in enumerate(s):
            if tmp[ch] == 1:
                return i
        return -1

s = "leetcode"
m = Solution()
m.firstUniqChar(s)