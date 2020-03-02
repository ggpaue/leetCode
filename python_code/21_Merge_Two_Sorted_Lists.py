#Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

#Example:

#Input: 1->2->4, 1->3->4
#Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        res = ListNode(0)
        head = res

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            res = res.next
        if l1 is not None:
            res.next = l1
        if l2 is not None:
            res.next = l2
        return head.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
print(l1.val, "->", l1.next.val, "->", l1.next.next.val)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
print(l2.val, "->", l2.next.val, "->", l2.next.next.val)

s = Solution()
print(s.mergeTwoLists(l1, l2))
