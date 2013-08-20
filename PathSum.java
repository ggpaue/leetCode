/**
 * 
 * Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

 * For example:
 * Given the below binary tree and sum = 22,
 *             5
 *            / \
 *           4   8
 *          /   / \
 *         11  13  4
 *        /  \      \
 *       7    2      1
 * return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
 * 
 * 
 * 
 */
import java.util.*;
public class Solution {
	public boolean hasPathSum(TreeNode root, int sum) {
		if(root == null) return false;
		Stack<TreeNode> nodes = new Stack<TreeNode>();
		Stack<Integer> accSums = new Stack<Integer>();
		nodes.add(root);
		accSums.add(root.val);
		while(!nodes.isEmpty()) {
			TreeNode node = nodes.pop();
			Integer accSum = accSums.pop();
			if(node.left == null && node.right == null && accSum == sum) return true;
			
			if(node.left != null) {
				nodes.add(node.left);
				accSums.add(accSum + node.left.val);
			}
			
			if(node.right != null) {
				nodes.add(node.right);
				accSums.add(accSum + node.right.val);
			}
		}
		
		return false;
		
		
	}
	
	

}
