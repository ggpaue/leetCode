#Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

#Example 1:
#Input:

#"bbbab"
#Output:
#4
#One possible longest palindromic subsequence is "bbbb".


#Example 2:
#Input:

#"cbbd"
#Output:
#2
#One possible longest palindromic subsequence is "bb".


#Constraints:

#1 <= s.length <= 1000
#s consists only of lowercase English letters.

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dp = [[0 for i in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1

        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][len(s)-1]