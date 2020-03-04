#Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

#If the last word does not exist, return 0.

#Note: A word is defined as a maximal substring consisting of non-space characters only.

#Example:

#Input: "Hello World"
#Output: 5

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        if s == "":
            return 0
        res = 0
        for i in range(len(s)-1, -1, -1):
            print(i)
            print(s[i])
            if s[i] == ' ' and res != 0:
                break
            elif s[i] != ' ':
                res += 1

        print(res)
        return res
        '''
        if len(s) == 0:
            return 0
        temp = s.split(' ')
        temp = [t for t in temp if len(t) > 0]
        if len(temp) == 0:
            return 0
        return len(temp[-1])



test = Solution()
s = "Hello World"
s2 = "a"
test.lengthOfLastWord(s)
test.lengthOfLastWord(s2)


