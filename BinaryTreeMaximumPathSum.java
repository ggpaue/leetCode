/**
 * 
 * @author GGPAUE
 * Given a binary tree, find the maximum path sum.

 * The path may start and end at any node in the tree.

 * For example:
 * Given the below binary tree,

 *      1
 *     / \
 *    2   3
 * Return 6.
 */


public class Solution {
	int invalid = -10000;
	int max;
	public int maxPathSum(TreeNode root) {	
		
		max = invalid;
		if(root == null) return 0;
		
		int result = maxPathSumHelper(root);
		
		if(result > max) max = result;
		return max;
	}
	
	public int maxPathSumHelper(TreeNode root) {
		if(root == null) return invalid;
		int left = maxPathSumHelper(root.left);
		int right = maxPathSumHelper(root.right);
		if(max < left) max = left;
		if(max < right) max = right;
		if(max < (root.val + left + right)) max = root.val + left + right;
		
		return Math.max(root.val, Math.max(root.val + left, root.val +right));
	}

}
