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
