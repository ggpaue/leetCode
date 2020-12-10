#Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

#The root is the maximum number in the array.
#The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
#The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
#Construct the maximum tree by the given array and output the root node of this tree.

#Example 1:
#Input: [3,2,1,6,0,5]
#Output: return the tree root node representing the following tree:

#      6
#    /   \
#   3     5
#    \    /
#     2  0
#       \
#        1
#Note:
#The size of the given array will be in the range [1,1000].

from typing import List
import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums == None:
            return None
        return self.build(nums, 0, len(nums)-1)

    def build(self, nums: List[int], low: int, high: int) -> TreeNode:
        if low > high:
            return None

        index = 0
        tmp = -sys.maxsize-1
        for i in range(low, high+1):
            if tmp < nums[i]:
                tmp = nums[i]
                index = i

        root = TreeNode(tmp)
        root.left = self.build(nums, low, index-1)
        root.right = self.build(nums, index+1, high)
        return root