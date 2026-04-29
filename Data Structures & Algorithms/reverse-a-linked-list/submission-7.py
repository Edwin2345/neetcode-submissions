# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #1 -> 2 -> 3 -> 4
        #n,p c
        #  p c    n
        #  p <-c  n
        #    pc   n
        #    p   cn

        prev = None
        nxt  = None
        curr = head
        while(curr != None):
            nxt = curr.next
            curr.next = prev        
            prev = curr
            curr = nxt
        
        return prev