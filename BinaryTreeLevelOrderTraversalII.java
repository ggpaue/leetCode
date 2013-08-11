/**
Binary Tree Level Order Traversal II
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
For example:
Given binary tree {3,9,20,#,#,15,7},
   3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:
[
  [15,7]
  [9,20],
  [3],
]

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
 **/

/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

import java.util.*;
public class Solution {
	public ArrayList<ArrayList<Integer>> levelOrderBottom(TreeNode root) {
		ArrayList<ArrayList<Integer>> record = new ArrayList<ArrayList<Integer>>();
		if(root == null) return record;
		HashMap<Integer, ArrayList<Integer>> map = new HashMap<Integer, ArrayList<Integer>>();
		int level = 0;
		visit(root, level, map);
		Set<Integer> set = map.keySet();
		
		int maxlevel = 0;
		for(int i : set) {
			maxlevel = Math.max(maxlevel, i);
		}
		for(int i = maxlevel; i >=0; i--) {
			ArrayList<Integer> list = map.get(i);
			record.add(list);
		}
		return record;
		
	}
	public static void visit(TreeNode node, int level, HashMap<Integer, ArrayList<Integer>> list) {
		if(list.containsKey(level) == false) {
			ArrayList<Integer> temp = new ArrayList<Integer>();
			list.put(level, temp);
		}
		ArrayList<Integer> record = list.get(level);
		record.add(node.val);
		if(node.left != null) visit(node.left, level+1, list);
		if(node.right != null) visit(node.right, level+1, list);
	}

}
