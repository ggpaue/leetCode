import java.util.*;
public class Solution {
	public ArrayList<Integer> preorderTraversalR(TreeNode root) {
		ArrayList<Integer> result = new ArrayList<Integer>();
		if(root == null) return result;
		pre(result, root);
		return result;
	}
	
	public void pre(ArrayList<Integer> res, TreeNode root) {
		res.add(root.val);
		if(root.left != null) {
			pre(res, root.left);
		}
		if(root.right != null) {
			pre(res, root.right);
		}
	}
	
	public ArrayList<Integer> preorderTraversalN(TreeNode root) {
		ArrayList<Integer> result = new ArrayList<Integer>();
		if(root == null) return result;
		Stack<TreeNode> st = new Stack<TreeNode>();
		st.push(root);
		while(!st.isEmpty()) {
			TreeNode current = st.peek();
			result.add(current.val);
			st.pop();
			if(current.right != null) {
				st.push(current.right);
			}
			if(current.left != null) {
				st.push(current.left);
			}
		}
		st = null;
		return result;
	}

}
