import java.util.*;
public class Solution {
	public ArrayList<ArrayList<Integer>> pathSum(TreeNode root, int sum) {
		ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
		if(root != null) {
			ArrayList<Integer> path = new ArrayList<Integer>();
			findPathSum(root, sum, result, path);
		}
		return result;
	}
	
	public void findPathSum(TreeNode root, int sum, ArrayList<ArrayList<Integer>> result, ArrayList<Integer> path) {
		if(root == null) return;
		if(root.left == null && root.right == null && root.val == sum) {
			ArrayList<Integer> clone = new ArrayList<Integer>(path);
			clone.add(root.val);
			result.add(clone);
		} else {
			path.add(root.val);
			if(root.left != null) {
				findPathSum(root.left, sum - root.val, result, path);
			} else if(root.right != null) {
				findPathSum(root.right, sum - root.val, result, path);
			}
			path.remove(path.size() - 1);
		}
	}
}
