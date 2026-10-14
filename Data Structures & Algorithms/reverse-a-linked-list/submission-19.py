# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def revList(cur, prev):
            if cur is None:
               return prev

            nxt = cur.next
            cur.next = prev

            return revList(nxt, cur)
        
        return revList(head, None)
