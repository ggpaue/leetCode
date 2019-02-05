/**
 * 
 * Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
 *
 * For example:
 * Given binary tree {3,9,20,#,#,15,7},
 *
 *     3
 *    / \
 *   9  20
 *     /  \
 *    15   7
 * return its zigzag level order traversal as:
 *
 * [
 *   [3],
 *   [20,9],
 *   [15,7]
 * ]
 * 
 */

import java.util.*;
public class Solution {
	public ArrayList<ArrayList<Integer>> zigzagLevelOrder(TreeNode root) {
		ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
		if(root == null) return result;
		boolean order = true;
		ArrayList<TreeNode> toVisit = new ArrayList<TreeNode>();
		toVisit.add(root);
		while(!toVisit.isEmpty()) {
			ArrayList<TreeNode> next = new ArrayList<TreeNode>();
			ArrayList<Integer> temp = new ArrayList<Integer>();
			for(TreeNode node : toVisit) {
				temp.add(node.val);
			}
			result.add(temp);
			for(int i = toVisit.size() - 1; i >= 0; i--) {
				TreeNode node = toVisit.get(i);
				if(order) {
					if(node.right != null) next.add(node.right);
					if(node.left != null) next.add(node.left);
				} else {
					if(node.left != null) next.add(node.left);
					if(node.right != null) next.add(node.right);
				}
			}
			order = order ? false : true;
			toVisit = new ArrayList<TreeNode>(next);
		}
		return result;
	}

}
