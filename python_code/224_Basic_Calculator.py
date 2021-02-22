#Given a string s representing an expression, implement a basic calculator to evaluate it.



#Example 1:

#Input: s = "1 + 1"
#Output: 2
#Example 2:

#Input: s = " 2-1 + 2 "
#Output: 3
#Example 3:

#Input: s = "(1+(4+5+2)-3)+(6+8)"
#Output: 23


#Constraints:

#1 <= s.length <= 3 * 105
#s consists of digits, '+', '-', '(', ')', and ' '.
#s represents a valid expression.

from typing import List
class Solution:
    def calculate(self, s: str) -> int:
        def helper(s: List) -> int:
            stack = []
            sign = '+'
            num = 0

            while len(s) > 0:
                c = s.pop(0)
                if c.isdigit():
                    num = 10*num + int(c)

                if c == '(':
                    num = helper(s)

                if (not c.isdigit() and c != ' ') or len(s) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        stack[-1] = int(stack[-1]/float(num))
                    num = 0
                    sign = c

                if c ==')':
                    break
            return sum(stack)

        return helper(list(s))

tmp = "1 + 1"
s = Solution()
print(s.calculate(tmp))