#Given a string num which represents an integer, return true if num is a strobogrammatic number.

#A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).



#Example 1:

#Input: num = "69"
#Output: true
#Example 2:

#Input: num = "88"
#Output: true
#Example 3:

#Input: num = "962"
#Output: false
#Example 4:

#Input: num = "1"
#Output: true


#Constraints:

#1 <= num.length <= 50
#num consists of only digits.
#num does not contain any leading zeros except for zero itself.

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        table = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        for index in range((len(num)+1)//2):
            if num[index] not in table or num[-index-1] != table[num[index]]:
                return False

        return True