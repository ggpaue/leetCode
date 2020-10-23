#Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

#Note: For the purpose of this problem, we define empty string as valid palindrome.

#Example 1:

#Input: "A man, a plan, a canal: Panama"
#Output: true
#Example 2:

#Input: "race a car"
#Output: false


#Constraints:

#s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        s = s.lower()

        while start <= end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            if start < end and s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

s = Solution()
tmp = "A man, a plan, a canal: Panama"
s.isPalindrome(tmp)
