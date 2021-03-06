/**
 * Given a binary tree, check whether it is a mirror of itself (ie, symmetric
 * around its center). For example, this binary tree is symmetric: 
 *    1 
 *   / \ 
 *  2   2 
 * / \ / \ 
 *3  4 4  3
 * 
 * But the following is not: 
 *    1 
 *   / \ 
 *  2   2 
 *   \   \ 
 *    3   3
 * 
 * Note: Bonus points if you could solve it both recursively and iteratively.
 * 
 * 
 * 
 * Definition for binary tree 
 * public class TreeNode { 
 * 		int val; 
 *      TreeNode left;
 *      TreeNode right; 
 *      TreeNode(int x) { 
 *      	val = x; 
 *      } 
 *  }
 */

import java.util.LinkedList;
public class Solution {
	public boolean isSymmetric(TreeNode root) {
		if(root == null) {
			return true;
		}
		return isSymmetric(root.left, root.right);
	}
	public boolean isSymmetric(TreeNode a, TreeNode b) {
		if(a == null) {
			return b == null;
		}
		if(b == null) {
			return false;
		}
		if(a.val != b.val) {
			return false;
		}
		if(!isSymmetric(a.left, b.right)) {
			return false;
		}
		if(!isSymmetric(a.right, b.left)) {
			return false;
		}
		return true;
	}
	
	
		public boolean isSymmetric(TreeNode root) {
			if(root == null) return true;
		LinkedList<TreeNode> l = new LinkedList<TreeNode>();
		LinkedList<TreeNode> r = new LinkedList<TreeNode>();
		l.add(root.left);
		r.add(root.right);
		while(!l.isEmpty() && !r.isEmpty()) {
			TreeNode temp1 = l.poll();
			TreeNode temp2 = r.poll();
			if(temp1 == null && temp2 != null || temp1 != null && temp2 == null)
				return false;
			if(temp1 != null) {
				if(temp1.val != temp2.val) {
					return false;
				}
				l.add(temp1.left);
				l.add(temp1.right);
				r.add(temp2.right);
				r.add(temp2.left);
			}
			
		}
		return true;
		}
	}


