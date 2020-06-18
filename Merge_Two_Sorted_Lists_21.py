# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        tracker = head

        while l1 and l2:
            if l1.val < l2.val:
                tracker.next = l1
                l1 = l1.next
            else:
                tracker.next = l2
                l2 = l2.next

            tracker = tracker.next

        if l1:
            tracker.next = l1
        else:
            tracker.next = l2

        return head.next
