/**
 * 
 * @author GGPAUE
 * Reverse a linked list from position m to n. Do it in-place and in one-pass.
 *
 * For example:
 * Given 1->2->3->4->5->NULL, m = 2 and n = 4,
 *
 * return 1->4->3->2->5->NULL.
 *
 * Note:
 * Given m, n satisfy the following condition:
 * 1 ? m ? n ? length of list.
 * 
 */

public class Solution {
	public ListNode reverseBetween(ListNode head, int m, int n) {
		if(head == null) return head;
		int start = 1;
		int end = 0;
		ListNode s = head;
		ListNode p = null;
		while(start++ < m && s != null) {
			p = s;
			s = s.next;
		}
		ListNode cur = null;
		ListNode next = null;
		ListNode prev = null;
		end = m;
		cur = s;
		while(end++ <= n && cur != null) {
			next = cur.next;
			cur.next = prev;
			prev = cur;
			cur = next;
		}
		s.next = cur;
		if(p != null) {
			p.next = prev;
			return head;
		} else {
			return prev;
		}
	}

}
