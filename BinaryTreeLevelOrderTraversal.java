/**
 * 
 * Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

 * For example:
 * Given binary tree {3,9,20,#,#,15,7},

 *    3
 *   / \
 *  9  20
 *    /  \
 *   15   7
 * return its level order traversal as:

 * [
 *  [3],
 *  [9,20],
 *  [15,7]
 * ]
 * 
 */


import java.util.*;
public class Solution {
	public ArrayList<ArrayList<Integer>> levelOrder(TreeNode root) {
		
		ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
		if(root == null) return result;
		
		Queue<TreeNode> queue = new LinkedList<TreeNode>();
		Map<TreeNode, Integer> map = new HashMap<TreeNode, Integer>();
		result.add(new ArrayList<Integer>());
		int level = 0, maxlevel = 0;
		queue.add(root);
		while(queue.isEmpty() == false) {
			TreeNode current = queue.poll();
			if(map.containsKey(current)) {
				level = map.get(current);
			} else {
				level = 0;
			}
			map.put(current, level);
			
			if(level > maxlevel) {
				maxlevel = level;
				ArrayList<Integer> list = new ArrayList<Integer>();
				list.add(current.val);
				result.add(list);
			} else {
				result.get(level).add(current.val);
			}
			
			if(current.left != null) {
				queue.add(current.left);
				map.put(current.left, level + 1);
			}
			
			if(current.right != null) {
				queue.add(current.right);
				map.put(current.right, level + 1);
			}
		}
		return result;
		
	}

}
