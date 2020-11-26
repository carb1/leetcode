# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        slow = fast = head
        while fast and fast.next:
            slow=slow.next
            fast = fast.next.next

        pre, cur = None, slow.next
        slow.next = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        p, q = head, pre
        while p and q:
            nxt = p.next
            p.next = q
            p = q
            q = nxt




