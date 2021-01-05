#Return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

#Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/



#Example 1:

#Input: s = "bcabc"
#Output: "abc"
#Example 2:

#Input: s = "cbacdcbc"
#Output: "acdb"


#Constraints:

#1 <= s.length <= 1000
#s consists of lowercase English letters.


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
        stack = []
        present = {}

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] -= 1

            if s[i] in present: continue

            while stack and count[ord(stack[-1]) - ord('a')] and ord(stack[-1]) > ord(s[i]):
                del present[stack[-1]]
                stack.pop()
            stack.append(s[i])
            present[s[i]] = True
        return "".join(stack)