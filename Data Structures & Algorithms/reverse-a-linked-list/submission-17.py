# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def revList(cur, prev):
            #base case, at end of list so new head is now prev
            if cur is None:
               return prev
            
            #reverse node
            nxtNode = cur.next
            cur.next = prev

            #go to next node
            return revList(nxtNode, cur)
        

        return revList(head, None)