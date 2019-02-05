/**
 * Given a binary tree, flatten it to a linked list in-place.

* For example,
* Given

         1
        / \
       2   5
      / \   \
     3   4   6
* The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
* Hints:
* If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.
 * Definition for binary tree 
 * 
 * public class TreeNode { 
 * 		int val; 
 * 		TreeNode left;
 * 		TreeNode right; 
 * 		TreeNode(int x) { 
 * 			val = x; 
 * 		} 
 * 	}
 * 
 */


import java.util.*;
public class Solution {
	public void flatten(TreeNode root) {
		if(root == null) return;
		ArrayList<Integer> list = new ArrayList<Integer>();
		convertBT2NodeList(list, root);
		root.left = null;
		TreeNode it = root;
		for(int i = 1; i < list.size(); i++) {
			it.right = new TreeNode(list.get(i));
			it.left = null;
			it = it.right;
		}
	}
	public static void convertBT2NodeList(ArrayList<Integer> list, TreeNode node) {
		int val = node.val;
		list.add(val);
		if(node.left != null) {
			convertBT2NodeList(list, node.left);
		}
		if(node.right != null) {
			convertBT2NodeList(list, node.right);
		}
	}

}
