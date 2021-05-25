#Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.



#Example 1:

#Input: s = "Hello"
#Output: "hello"
#Example 2:

#Input: s = "here"
#Output: "here"
#Example 3:

#Input: s = "LOVELY"
#Output: "lovely"


#Constraints:

#1 <= s.length <= 100
#s consists of printable ASCII characters.
import string
class Solution:
    def toLowerCase(self, s: str) -> str:
        if not s:
            return None

        #return s.lower()
        return "".join(chr(ord(c) - ord('A') + ord('a')) if c >= "A" and c <= "Z" else c for c in s)