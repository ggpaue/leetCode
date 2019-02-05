/**
 * 
 * @author GGPAUE
 *
 * Follow up for problem "Populating Next Right Pointers in Each Node".

 * What if the given tree could be any binary tree? Would your previous solution still work?

 * Note:

 * You may only use constant extra space.
 * For example,
 * Given the following binary tree,

 *          1
 *        /  \
 *       2    3
 *      / \    \
 *     4   5    7
 * After calling your function, the tree should look like:

 *          1 -> NULL
 *        /  \
 *       2 -> 3 -> NULL
 *      / \    \
 *     4-> 5 -> 7 -> NULL
 */


public class Solution {
	public void connect(TreeLinkNode root) {
		TreeLinkNode currentBegin = root;
		TreeLinkNode prevBegin = null;
		while(currentBegin != null) {
			TreeLinkNode curr = currentBegin;
			while(curr != null) {
				TreeLinkNode next = null;
				while(prevBegin != null) {
					if(prevBegin.left != null && prevBegin.left != curr) {
						next = prevBegin.left;
						break;
					} else if(prevBegin.right != null && prevBegin.right != curr) {
						next = prevBegin.right;
						prevBegin = prevBegin.next;
						break;
					} else {
						prevBegin = prevBegin.next;
					}
				}
				curr.next = next;
				curr = curr.next;
			}
			prevBegin = currentBegin;
			currentBegin = null;
			TreeLinkNode node = prevBegin;
			while(node != null) {
				if(node.left != null) {
					currentBegin = node.left;
					break;
				} else if(node.right != null) {
					currentBegin = node.right;
					break;
				} else {
					node = node.next;
				}
			}
		}
	}

}
