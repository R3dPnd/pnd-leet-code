from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        fake_head = ListNode(0)
        curr = fake_head

        while list1 and list2:
            print(f"{list1.val}:{list2.val}")
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
        curr.next = list1 if list1 else list2
                
        return fake_head.next