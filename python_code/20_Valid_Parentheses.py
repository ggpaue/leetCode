#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Note that an empty string is also considered valid.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        tmp = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                tmp.append(c)
            elif c == ')':
                if not tmp or tmp.pop() != '(':
                    return False
            elif c == '}':
                if not tmp or tmp.pop() != '{':
                    return False
            else:
                if not tmp or tmp.pop() != '[':
                    return False
        return not tmp

s = Solution()
test = "()[]{}"
s.isValid(test)

