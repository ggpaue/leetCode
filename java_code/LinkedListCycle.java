
public class Solution {
	public boolean hasCycle(ListNode head) {
		if(head == null) return false;
		ListNode slow = head;
		ListNode fast = head;
		
		while(true) {
			slow = slow.next;
			if(fast.next != null) {
				fast = fast.next.next;
			} else {
				return false;
			}
			if(slow == null || fast == null) return false;
			if(slow == fast) return true;
		}
	}

}
