""" 24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None: return
        curr,i, result  = head, 0, head
        while (curr.next is not None):
            # before the nodes are swapped, save the ListNode to return
            if curr is head: result = curr.next

            # swap the pointers
            Solution.swapPointers(self, curr, curr.next)

            # before: 1->2->3->4, now: 2->1->3->4
            # need to attach 1 to 4: 2->1->4<-3 (note, 3 is pointing to 4)
            # then change curr to 3
            if curr.next is not None and curr.next.next is not None:
                temp = curr.next
                curr.next = curr.next.next
                curr = temp
            else: break
        return result

    # swaps the pointers of two ListNodes
    # 1->2->3 becomes 2->1->3, nodes 1 and 2 are swapped
    def swapPointers(self, p1: ListNode, p2:ListNode):
        temp = p2.next
        p2.next = p1
        p1.next = temp
        