/**
 * 
 * @author GGPAUE
 * You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
 *
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 *
 */

public class Solution {
	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		if(l1 == null) return l2;
		if(l2 == null) return l1;
		ListNode head = new ListNode(0);
		ListNode curr = head;
		int carry = 0;
		
		while(l1 != null && l2 != null) {
			int sum = l1.val + l2.val + carry;
			carry = sum / 10;
			sum = sum % 10;
			curr.next = new ListNode(sum);
			curr = curr.next;
			l1 = l1.next;
			l2 = l2.next;
		}
		
		if(l1 != null) {
			if(carry != 0) {
				curr.next = addTwoNumbers(l1, new ListNode(carry));
			} else {
				curr.next = l1;
			}
		} else if(l2 != null) {
			if(carry != 0) {
				curr.next = addTwoNumbers(l2, new ListNode(carry));
			} else {
				curr.next = l2;
			}
		} else if(carry != 0) {
			curr.next = new ListNode(carry);
		}
		
		return head.next;
	}

}
