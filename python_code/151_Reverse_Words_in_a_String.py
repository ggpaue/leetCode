#Given an input string s, reverse the order of the words.

#A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

#Return a string of the words in reverse order concatenated by a single space.

#Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.



#Example 1:

#Input: s = "the sky is blue"
#Output: "blue is sky the"
#Example 2:

#Input: s = "  hello world  "
#Output: "world hello"
#Explanation: Your reversed string should not contain leading or trailing spaces.
#Example 3:

#Input: s = "a good   example"
#Output: "example good a"
#Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
#Example 4:

#Input: s = "  Bob    Loves  Alice   "
#Output: "Alice Loves Bob"
#Example 5:

#Input: s = "Alice does not even like bob"
#Output: "bob like even not does Alice"


#Constraints:

#1 <= s.length <= 104
#s contains English letters (upper-case and lower-case), digits, and spaces ' '.
#There is at least one word in s.


#Follow up: Could you solve it in-place with O(1) extra space?

class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 1:
            return s
        l, r = 0, len(s) - 1
        tmp = []
        res = ''
        while s[l] == ' ':
            l += 1
        while s[r] == ' ':
            r -= 1

        end = r + 1
        r = l + 1
        while r < end:
            if s[r] == ' ':
                tmp.append(s[l:r])
                while s[r] == ' ':
                    r += 1
                l = r
                r = l + 1
            else:
                r += 1
        tmp.append(s[l:r])
        res = tmp.pop()
        while tmp:
            res = res + ' ' + tmp.pop()
        return res
