#Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

#'?' Matches any single character.
#'*' Matches any sequence of characters (including the empty sequence).
#The matching should cover the entire input string (not partial).



#Example 1:

#Input: s = "aa", p = "a"
#Output: false
#Explanation: "a" does not match the entire string "aa".
#Example 2:

#Input: s = "aa", p = "*"
#Output: true
#Explanation: '*' matches any sequence.
#Example 3:

#Input: s = "cb", p = "?a"
#Output: false
#Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
#Example 4:

#Input: s = "adceb", p = "*a*b"
#Output: true
#Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
#Example 5:

#Input: s = "acdcb", p = "a*c?b"
#Output: false


#Constraints:

#0 <= s.length, p.length <= 2000
#s contains only lowercase English letters.
#p contains only lowercase English letters, '?' or '*'.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[0 for i in range(len(p)+1)] for _ in range(len(s)+1)]
        dp[0][0] = 1

        for j in range(1, len(p)+1):
            if p[j-1] != '*':
                break
            dp[0][j] = 1

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] in {s[i-1], '?'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]

    def isMatchSim(self, s: str, p: str) -> bool:
        if p == '*':
            return True
        index = 0
        for i in range(len(p)):
            if p[i] == '*':
                index = i

        tmp = p[:index] + p[index+1:]
        if len(s) < len(tmp):
            return False

        if index != 0 and index != len(p) - 1:
            if s.startswith(p[:index]) and s.endswith(p[index + 1:]):
                return True
        if index == 0:
            return s.endswith(p[1:])
        if index == len(p) - 1:
            return s.startswith(p[:-1])
        return False







s = Solution()
tmp = "cat"
p = "cat*"
print(s.isMatchSim(tmp, p))