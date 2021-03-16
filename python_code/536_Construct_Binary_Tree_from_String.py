#You need to construct a binary tree from a string consisting of parenthesis and integers.

#The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

#You always start to construct the left child node of the parent first if it exists.



#Example 1:


#Input: s = "4(2(3)(1))(6(5))"
#Output: [4,2,6,3,1,5]
#Example 2:

#Input: s = "4(2(3)(1))(6(5)(7))"
#Output: [4,2,6,3,1,5,7]
#Example 3:

#Input: s = "-4(2(3)(1))(6(5)(7))"
#Output: [-4,2,6,3,1,5,7]


#Constraints:

#0 <= s.length <= 3 * 104
#s consists of digits, '(', ')', and '-' only.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        n = len(s)
        preroot = TreeNode()
        stack = [preroot]

        l, r = 0, 0
        while l < n:
            if s[l] in ['(', ')']:
                if s[l] == ')':
                    stack.pop()
                r += 1
            else:
                while r < n and s[r] not in ['(', ')']:
                    r += 1

                curr = TreeNode(int(s[l:r]))
                if stack[-1].left:
                    stack[-1].right = curr
                else:
                    stack[-1].left = curr
                stack.append(curr)
            l = r
        return preroot.left