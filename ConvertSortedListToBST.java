/**
Convert Sorted List to Binary Search Tree
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
**/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 
public class Solution {
    
	public int calLen(ListNode head) {
		int length = 0;
		while(head != null) {
			length++;
			head = head.next;
		}
		return length;
	}
	public TreeNode createTree(ListNode head, int left, int right) {
		ListNode node = head;
        if(head == null || left > right) return null;
		int mid = (right - left) / 2;
		for(int i = 0; i < mid; i++) {
			node = node.next;
		}
        
		TreeNode root = new TreeNode(node.val);
		root.left = createTree(head, left, left+mid-1);
		root.right = createTree(node.next, left+mid+1, right);
		return root;
	}
	public TreeNode sortedListToBST(ListNode head) {
		int len = calLen(head);
		return createTree(head, 0, len-1);
	}

}
