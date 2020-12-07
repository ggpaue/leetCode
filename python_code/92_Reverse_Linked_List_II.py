#Reverse a linked list from position m to n. Do it in one-pass.

#Note: 1 ≤ m ≤ n ≤ length of list.

#Example:

#Input: 1->2->3->4->5->NULL, m = 2, n = 4
#Output: 1->4->3->2->5->NULL

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        '''

        :param head:
        :param m:
        :param n:
        :return:
        pre = dummy = ListNode(0)
        dummy.next = head

        for _ in range(m-1):
            pre = pre.next

        cur = pre.next
        for _ in range(m, n):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
        return dummy.next
        '''

        if head is None:
            return None
        if head.next is None:
            return head
        successor = ListNode(0)
        def reverseN(head: ListNode, n: int) -> ListNode:
            nonlocal successor
            if n == 1:
                successor = head.next
                return head

            last = reverseN(head.next, n-1)
            head.next.next = head
            head.next = successor
            return last

        if m == 1:
            return reverseN(head, n)

        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head

