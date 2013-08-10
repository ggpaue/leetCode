/**
 * 
 * Remove Duplicates from Sorted ListApr 22 '12
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
 * 
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
 
public class Solution {
    
    public ListNode deleteDuplicates(ListNode head) {
		if(head == null) return null;
		if(head.next == null) return head;
		
		
		while(head.next != null) {
			if(head.next.val != head.val) {
				break;
			} else {
				head.next = head.next.next;
			}
		}
		
		head.next = deleteDuplicates(head.next);
		return head;
	}

}
