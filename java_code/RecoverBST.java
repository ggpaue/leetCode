/**
 * 
 * Two elements of a binary search tree (BST) are swapped by mistake.
 *
 * Recover the tree without changing its structure.
 *
 * Note:
 * A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
 *
 * OJ's Binary Tree Serialization:
 * The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.
 *
 * Here's an example:
 *
 *    1
 *   / \
 *  2   3
 *     /
 *    4
 *     \
 *      5
 * The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".
 *  
 */

import java.util.*;
public class Solution {
	public void recoverTree(TreeNode root) {
		if(root == null) return;
		ArrayList<TreeNode> nodes = new ArrayList<TreeNode>();
		findWrongNode(root, nodes);
		TreeNode a = null, b = null;
		
		int i = 0;
		
		for(i = 0; i < nodes.size() - 1; i++) {
			if(nodes.get(i).val > nodes.get(i + 1).val) {
				a = nodes.get(i);
				break;
			}
		}
		
		for(int j = i + 1; j < nodes.size() - 1; j++) {
			if(nodes.get(j).val > nodes.get(j + 1).val) {
				b = nodes.get(j + 1);
				break;
			}
		}
		
		if(b == null) b = nodes.get(i + 1);
		
		int t = a.val;
		a.val = b.val;
		b.val = t;
	}
	
	private void findWrongNode(TreeNode root, ArrayList<TreeNode> nodes) {
		if(root == null) return;
		findWrongNode(root.left, nodes);
		nodes.add(root);
		findWrongNode(root.right, nodes);
	}

}
