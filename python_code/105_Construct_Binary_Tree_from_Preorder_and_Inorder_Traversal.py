#Given preorder and inorder traversal of a tree, construct the binary tree.

#Note:
#You may assume that duplicates do not exist in the tree.

#For example, given

#preorder = [3,9,20,15,7]
#inorder = [9,3,15,20,7]
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder is None or inorder is None:
            return None
        return self.build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)

    def build(self, preorder: List[int], preStart: int, preEnd: int, inorder: List[int], inStart: int, inEnd: int) -> TreeNode:
        if preStart > preEnd:
            return None

        rootVal = preorder[preStart]
        index = 0
        for i in range(inStart, inEnd+1):
            if inorder[i] == rootVal:
                index = i
                break

        leftSize = index - inStart
        root = TreeNode(rootVal)
        root.left = self.build(preorder, preStart+1, preStart+leftSize, inorder, inStart, index-1)
        root.right = self.build(preorder, preStart+leftSize+1, preEnd, inorder, index+1, inEnd)

        return root
