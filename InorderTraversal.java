/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.util.Stack;
public class solution {
	public ArrayList<Integer> inorderTraversal(TreeNode root) {
        // Start typing your Java solution below
        // DO NOT write main() function
        	ArrayList<Integer> result = new ArrayList<Integer>();
        	if(root == null){
        		return result;
        	}
       
        	Stack<TreeNode> stack = new Stack<TreeNode>();
        	TreeNode current;
        	while(true){
        		while(root != null){
        			stack.push(root);
        			root = root.left;
        		}
            if(stack.empty())
            	break;
            	root = stack.pop();
            	result.add(root.val);
            
            if(root.right!= null) {
                root = root.right;
            } else{
                root = null;
            }
        }
             
        return result;
                    
    }

}
