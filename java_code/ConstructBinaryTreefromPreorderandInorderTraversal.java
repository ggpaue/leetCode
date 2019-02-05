/**
 * 
 * @author GGPAUE
 * Given preorder and inorder traversal of a tree, construct the binary tree.
 *
 * Note:
 * You may assume that duplicates do not exist in the tree.
 */

public class Solution {
	public TreeNode buildTree(int[] preorder, int[] inorder) {
		return buildTree(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1);
	}
	
	public TreeNode buildTree(int[] preorder, int ps, int pe, int[] inorder, int is, int ie) {
		if(ps > pe || is > ie) return null;
		int rootVal = preorder[ps];
		TreeNode root = new TreeNode(rootVal);
		for(int i = is; i <= ie; i++) {
			if(inorder[i] == rootVal) {
				TreeNode left = buildTree(preorder, ps + 1, ps + i - is, inorder, is, i - 1);
				TreeNode right = buildTree(preorder, ps + i - is + 1, pe, inorder, i + 1, ie);
				root.left = left;
				root.right = right;
			}
		}
		return root;
	}

}
