#Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

#Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/



#Example 1:

#Input: s = "bcabc"
#Output: "abc"
#Example 2:

#Input: s = "cbacdcbc"
#Output: "acdb"


#Constraints:

#1 <= s.length <= 104
#s consists of lowercase English letters.

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
        stack = []
        present = {}
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] -= 1

            if s[i] in present: continue

            while stack and ord(stack[-1]) > ord(s[i]) and count[ord(stack[-1])-ord('a')]:
                del present[stack[-1]]
                stack.pop()
            stack.append(s[i])
            present[s[i]] = True
        return "".join(stack)
a = Solution()
s = "cbacdcbc"
a.removeDuplicateLetters(s)

