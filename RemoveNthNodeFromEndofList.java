/**
 * Given a linked list, remove the nth node from the end of list and return its head.

 * For example,

 * Given linked list: 1->2->3->4->5, and n = 2.

 * After removing the second node from the end, the linked list becomes 1->2->3->5.
 * Note:
 * Given n will always be valid.
 * Try to do this in one pass.
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
 * 
 */

public class Solution {
	public ListNode removeNthFromEnd(ListNode head, int n) {
		ListNode front = head;
		int count;
		for(count = 0; count < n; count++) {
			if(front == null) break;
			front = front.next;
		}
		if(count < n) {  // List is not long enough
			return head;
		} else if(front == null) {  // List is exactly with length ==n remove the head
			return head.next;
		} else {
			front = front.next;
			ListNode toBeRemoved = head.next;
			ListNode back = head;
			while(front != null) {
				front = front.next;
				toBeRemoved = toBeRemoved.next;
				back = back.next;
			}
			if(toBeRemoved != null) {   // n is not 1
				back.next = toBeRemoved.next;
			} else {  // n is 1
				back.next = null;
			}
			return head;
		}
	}

}
