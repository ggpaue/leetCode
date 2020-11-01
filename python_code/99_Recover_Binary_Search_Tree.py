#You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

#Follow up: A solution using O(n) space is pretty straight forward; could you devise a constant space solution?

#Example 1:
#Input: root = [1,3,null,null,2]
#Output: [3,1,null,null,2]

#Example 2:
#Input: root = [3,1,4,null,null,2]
#Output: [2,1,4,null,null,3]

#Constraints:

#The number of nodes in the tree is in the range [2, 1000].
#-231 <= Node.val <= 231 - 1


from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(r: TreeNode) -> List[int]:
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        def find_swap(nums: List[int]) -> (int, int):
            x = y = -1
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    y = nums[i+1]
                    if x == -1:
                        x = nums[i]
                    else:
                        break
            return x, y

        def recover(r: TreeNode, count: int):
            if r:
                if r.val == x or r.val == y:
                    r.val = y if r.val == x else x
                    count -= 1
                    if count == 0:
                        return
                recover(r.left, count)
                recover(r.right, count)

        nums = inorder(root)
        x, y = find_swap(nums)
        recover(root, 2)


