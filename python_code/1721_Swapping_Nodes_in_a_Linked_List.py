#You are given the head of a linked list, and an integer k.

#Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).



#Example 1:


#Input: head = [1,2,3,4,5], k = 2
#Output: [1,4,3,2,5]
#Example 2:

#Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
#Output: [7,9,6,6,8,7,3,0,9,5]
#Example 3:

#Input: head = [1], k = 1
#Output: [1]
#Example 4:

#Input: head = [1,2], k = 1
#Output: [2,1]
#Example 5:

#Input: head = [1,2,3], k = 2
#Output: [1,2,3]


#Constraints:

#The number of nodes in the list is n.
#1 <= k <= n <= 105
#0 <= Node.val <= 100

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        node1, node2, node3 = head, head, head
        i = 1
        while i < k:
            node1 = node1.next
            i += 1

        j = 1
        while j < k:
            node2 = node2.next
            j += 1
        while node2.next:
            node2 = node2.next
            node3 = node3.next

        node1.val, node3.val = node3.val, node1.val
        return head
