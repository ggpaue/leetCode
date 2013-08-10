
public class Solution {
	public int maxDepth(TreeNode root) {
		int record = 0;
		preorder(root,1);
		return record;
	}
	private static int record = 0;
	private static void preorder(TreeNode root, int height) {
		if(root == null) {
			record = 0;
			return;
		}
		if(root.left == null && root.right == null) {
			if (height > record) {
				record = height;
			}
		} else {
			if(root.left != null) {
				preorder(root.left, height+1);
			}
			if(root.right != null) {
				preorder(root.right, height+1);
			}
		}
	}

}
