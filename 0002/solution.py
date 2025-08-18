from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        n = 0
        l1_sum = 0

        while curr:
            l1_sum += curr.val * pow(10,n)
            curr = curr.next
            n+=1

        curr = l2
        n = 0
        l2_sum = 0

        while curr:
            l2_sum += curr.val * pow(10,n)
            curr = curr.next
            n+=1
        
        # Return the result list (skip the dummy head)
        sum = l1_sum + l2_sum

        head = None
        while sum > 0:
            place_val = sum % 10
            sum = sum // 10
            new_node = ListNode(place_val)
            new_node.next = head
            head = new_node
        return head
