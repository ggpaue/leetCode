/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { 
 *     		val = x; 
 *     }
 * }
 */

public class Solution {
	public boolean isSameTree(TreeNode p, TreeNode q) {
		if(p != null && q == null) return false;
		if(p == null && q != null) return false;
		if(p == null && q == null) return true;
		boolean left = isSameTree(p.left, q.left);
		boolean right = isSameTree(p.right, q.right);
		return left && right && p.val == q.val;
	}

}
