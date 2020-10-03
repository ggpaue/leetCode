# Given a string s, find the length of the longest substring without repeating characters.
#
#
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:
#
# Input: s = ""
# Output: 0
#
#
# Constraints:
#
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        i = 0
        j = 0
        tmp = set()
        while i < len(s) and j < len(s):
            if s[j] not in tmp:
                tmp.add(s[j])
                res = max(res, j - i + 1)
                j += 1
            else:
                tmp.remove(s[i])
                i += 1
        return res

s = Solution()
tmp = "pwwkew"
s.lengthOfLongestSubstring(tmp)

