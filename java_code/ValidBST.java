/**
 * Given a binary tree, determine if it is a valid binary search tree (BST).

 * Assume a BST is defined as follows:

 * The left subtree of a node contains only nodes with keys less than the node's key.
 * The right subtree of a node contains only nodes with keys greater than the node's key.
 * Both the left and right subtrees must also be binary search trees.

 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

public class Solution {
    public boolean isValidBST(TreeNode root) {
		if(root == null) {
			return true;
		} else {
			return isValid(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
		}
	}
	public static boolean isValid(TreeNode root, int low, int high) {
		int val = root.val;
		if(val >= high || val <= low) {
			return false;
		}
		boolean flag = true;
		if(root.left != null) {
			flag = isValid(root.left, low, val);
			if(!flag) return flag;
		}
		if(root.right != null) {
			flag = isValid(root.right, val, high);
			if(!flag) return flag;
		}
		return true;
	}
}