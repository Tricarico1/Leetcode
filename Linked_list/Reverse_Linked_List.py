# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # I want to switch the path of these by creating a dummy node then deleting the dummy node recursively 
        d = ListNode("temp")
        d.next = head

        prev = None
        current = head
    
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        return d.next