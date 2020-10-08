# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

    示例：

    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        re = ListNode(0)
        r = re
        sign = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + sign
            sign = s // 10
            r.next = ListNode(s % 10)
            r = r.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if sign > 0:
            r.next = ListNode(1)
        return re.next

    def addTwoNumbers_1(self, l1, l2):
        """
        test.addTwoNumbers_1([2, 4, 3], [9, 6, 4])
        """
        res = []
        key = -1
        index = 0
        sign = 0
        while index < len(l1) or index < len(l2):
            x = l1[key] if abs(key) <= len(l1) else 0
            y = l2[key] if abs(key) <= len(l2) else 0
            res.append((x + y + sign) % 10)
            sign = (x + y + sign) // 10
            key -= 1
            index += 1
        if sign > 0:
            res.append(1)
        return res


def lst_to_lnd(lst):
    res = ListNode(lst[0])
    for i in range(1, len(lst)):
        res = ListNode(lst[i], res)
    return res


if __name__ == '__main__':
    test = Solution()
    l1 = lst_to_lnd([2, 4, 3])
    l2 = lst_to_lnd([5, 6, 4])
    print(test.addTwoNumbers(l1, l2).val)
    print(test.addTwoNumbers(l1, l2).next.val)
    print(test.addTwoNumbers(l1, l2).next.next.val)

