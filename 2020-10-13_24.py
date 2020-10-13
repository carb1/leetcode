# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

    你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

     

    示例 1：


    输入：head = [1,2,3,4]
    输出：[2,1,4,3]
    示例 2：

    输入：head = []
    输出：[]
    示例 3：

    输入：head = [1]
    输出：[1]
    """
    def swapPairs(self, head):
        re = ListNode(-1)
        re.next = head
        cge = re
        while cge.next and cge.next.next:
            a, b = cge.next, cge.next.next
            cge.next = b
            a.next = b.next
            b.next = a
            cge = cge.next.next
        return re.next

    def swapPairs_2(self, head):
        if not head or not head.next:
            return head
        first = head
        second = head.next
        first.next = self.swapPairs_2(second.next)
        second.next = first
        return second
