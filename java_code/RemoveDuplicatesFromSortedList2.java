/**
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
		if(head == null) {
			return null;
		}
		
		boolean flag = true; 
		while(head.next != null) {
			if(head.next.val == head.val)  flag = false;
				else break;
				head.next = head.next.next;		
		}
		if(flag == true) {
			head.next = deleteDuplicates(head.next);
			return head;
		} else {
			if(head.next == null) {
				return null;
			}
		return deleteDuplicates(head.next);
		}	
	}

}
