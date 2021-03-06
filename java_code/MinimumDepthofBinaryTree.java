/**

Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
	public int minDepth(TreeNode root) {
		if(root == null) return 0;
		record = Integer.MAX_VALUE;
		solve(root, 1);
		return record;
	}
	private static int record;
	private static void solve(TreeNode root, int height) {
		if(root.left == null && root.right == null) {
			if(height < record) {
				record = height;
			}
		} else {
			if(root.left != null) {
				solve(root.left, height+1);
			}
			if(root.right != null) {
				solve(root.right, height+1);
			}
		}
	}
}
