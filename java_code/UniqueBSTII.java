/**
 * 
 * Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

 * For example,
 * Given n = 3, your program should return all 5 unique BST's shown below.

 *   1         3     3      2      1
 *    \       /     /      / \      \
 *     3     2     1      1   3      2
 *    /     /       \                 \
 *   2     1         2                 3
 * 
 */

import java.util.*;
public class Solution {
	public ArrayList<TreeNode> generateTrees(int n) {
		ArrayList<TreeNode> result = dfs(1, n);
		return result;
	}
	
	private ArrayList<TreeNode> dfs(int min, int max) {
		ArrayList<TreeNode> result = new ArrayList<TreeNode>();
		if(max < min) {
			result.add(null);
			return result;
		} else if(min == max) {
			TreeNode root = new TreeNode(min);
			result.add(root);
			return result;
		} else {
			for(int i = min; i <= max; i++) {
				ArrayList<TreeNode> left = dfs(min, i - 1);
				ArrayList<TreeNode> right = dfs(i + 1, max);
				for(TreeNode l : left) {
					for(TreeNode r : right) {
						TreeNode t = new TreeNode(i);
						t.left = l;
						t.right = r;
						result.add(t);
					}
				}
			}
			return result;
		}
	}

}
