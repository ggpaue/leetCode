#Given a singly linked list, determine if it is a palindrome.

#Example 1:

#Input: 1->2
#Output: false
#Example 2:

#Input: 1->2->2->1
#Output: true
#Follow up:
#Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(head: ListNode) -> ListNode:
            pre = None
            cur = head
            while cur is not None:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre

        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        if fast is not None:
            slow = slow.next

        left = head
        right = reverse(slow)

        while right is not None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

