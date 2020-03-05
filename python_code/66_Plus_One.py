#Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

#The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

#You may assume the integer does not contain any leading zero, except the number 0 itself.

#Example 1:

#Input: [1,2,3]
#Output: [1,2,4]
#Explanation: The array represents the integer 123.
#Example 2:

#Input: [4,3,2,1]
#Output: [4,3,2,2]
#Explanation: The array represents the integer 4321.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

        if digits == []:
            return []
        tmp = 1
        i = len(digits) - 1
        while i >= 0:
            digits[i] += tmp
            tmp = 0
            if digits[i] == 10:
                digits[i] = 0
                tmp = 1
                i -= 1
            else:
                break
        if tmp == 1:
            digits.insert(0, tmp)
        print(digits)
        return digits
        """
        m = len(digits)
        for index in reversed(range(m)):
            if digits[index] < 9:
                digits[index] += 1
                print(digits)
                return digits
            else:
                digits[index] = 0
        digits.insert(0, 1)
        print(digits)
        return digits


s = Solution()
#digits = [1,2,3]
#digits = [4,3,2,1]
digits = [0]
s.plusOne(digits)