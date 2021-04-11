#Given the root of a binary tree, return the sum of values of its deepest leaves.


#Example 1:


#Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
#Output: 15
#Example 2:

#Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
#Output: 19


#Constraints:

#The number of nodes in the tree is in the range [1, 104].
#1 <= Node.val <= 100
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = deque([root])
        res = 0

        while queue:
            qlen, res = len(queue), 0
            for _ in range(qlen):
                curr = queue.popleft()
                res += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return res
