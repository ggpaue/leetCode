#Given inorder and postorder traversal of a tree, construct the binary tree.

#Note:
#You may assume that duplicates do not exist in the tree.

#For example, given

#inorder = [9,3,15,20,7]
#postorder = [9,15,7,20,3]
#Return the following binary tree:

#    3
#   / \
#  9  20
#    /  \
#   15   7

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder is None or postorder is None:
            return None
        return self.build(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)

    def build(self, inorder: List[int], inStart: int, inEnd: int, postorder: List[int], postStart: int, postEnd: int) -> TreeNode:
        if inStart > inEnd:
            return None

        rootVal = postorder[postEnd]
        index = 0
        for i in range(inStart, inEnd + 1):
            if inorder[i] == rootVal:
                index = i
                break

        leftSize = index - inStart
        root = TreeNode(rootVal)
        root.left = self.build(inorder, inStart, index-1, postorder, postStart, postStart+leftSize-1)
        root.right = self.build(inorder, index+1, inEnd, postorder, postStart+leftSize, postEnd-1)
        return root

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
s = Solution()
s.buildTree(inorder, postorder)