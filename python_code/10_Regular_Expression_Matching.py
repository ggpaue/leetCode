#Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where:

#'.' Matches any single character.​​​​
#'*' Matches zero or more of the preceding element.
#The matching should cover the entire input string (not partial).



#Example 1:

#Input: s = "aa", p = "a"
#Output: false
#Explanation: "a" does not match the entire string "aa".
#Example 2:

#Input: s = "aa", p = "a*"
#Output: true
#Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
#Example 3:

#Input: s = "ab", p = ".*"
#Output: true
#Explanation: ".*" means "zero or more (*) of any character (.)".
#Example 4:

#Input: s = "aab", p = "c*a*b"
#Output: true
#Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
#Example 5:

#Input: s = "mississippi", p = "mis*is*p*."
#Output: false


#Constraints:

#0 <= s.length <= 20
#0 <= p.length <= 30
#s contains only lowercase English letters.
#p contains only lowercase English letters, '.', and '*'.
#It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = dict()
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)
            # check fist character match
            first = i < len(s) and p[j] in {s[i], '.'}
            if j <= len(p) - 2 and p[j+1] == '*':
                # * appears in p
                # match 0 time or match 1 time and continue the match process
                ans = dp(i, j+2) or first and dp(i+1, j)
            else:
                # no * and continue the character match
                ans = first and dp(i+1, j+1)
            memo[(i, j)] = ans
            return ans

        return dp(0, 0)
