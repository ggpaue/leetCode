#Given two strings text1 and text2, return the length of their longest common subsequence.

#A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.


#If there is no common subsequence, return 0.

#Example 1:

#Input: text1 = "abcde", text2 = "ace"
#Output: 3
#Explanation: The longest common subsequence is "ace" and its length is 3.
#Example 2:

#Input: text1 = "abc", text2 = "abc"
#Output: 3
#Explanation: The longest common subsequence is "abc" and its length is 3.
#Example 3:

#Input: text1 = "abc", text2 = "def"
#Output: 0
#Explanation: There is no such common subsequence, so the result is 0.


#Constraints:

#1 <= text1.length <= 1000
#1 <= text2.length <= 1000
#The input strings consist of lowercase English characters only.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = ' ' + text1
        text2 = ' ' + text2
        print(text1)
        print(text2)

        dp = [[0 for i in range(len(text2))] for j in range(len(text1)) ]
        print(dp)
        tmp = 0
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                tmp += 1
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    print(tmp, dp)
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    print(tmp, dp)
        print(dp[-1][-1])
        return dp[-1][-1]

s = Solution()
text1 = "abcde"
text2 = "ace"
#dp = [[0 for i in range(len(text1))] for j in range(len(text2))]
#print(dp)
s.longestCommonSubsequence(text1, text2)