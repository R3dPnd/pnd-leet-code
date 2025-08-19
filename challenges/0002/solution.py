from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_over = 0

        new_head = ListNode(0)
        curr = new_head
        while l1 != None or l2 != None or carry_over != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            column_sum = l1Val +l2Val + carry_over
            carry_over = column_sum // 10
            newNode = ListNode(column_sum%10)
            curr.next= newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return new_head.next
