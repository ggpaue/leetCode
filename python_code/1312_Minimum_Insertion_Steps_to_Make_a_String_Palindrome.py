#Given a string s. In one step you can insert any character at any index of the string.

#Return the minimum number of steps to make s palindrome.

#A Palindrome String is one that reads the same backward as well as forward.



#Example 1:

#Input: s = "zzazz"
#Output: 0
#Explanation: The string "zzazz" is already palindrome we don't need any insertions.
#Example 2:

#Input: s = "mbadm"
#Output: 2
#Explanation: String can be "mbdadbm" or "mdbabdm".
#Example 3:

#Input: s = "leetcode"
#Output: 5
#Explanation: Inserting 5 characters the string becomes "leetcodocteel".
#Example 4:

#Input: s = "g"
#Output: 0
#Example 5:

#Input: s = "no"
#Output: 1


#Constraints:

#1 <= s.length <= 500
#All characters of s are lower case English letters.

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
        return dp[0][n-1]