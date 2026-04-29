# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       #edge case -> empty list
       if not head:
         return None

       #insert dummy node to make window work
       dummy = ListNode(-1,head) 
       L = dummy
       R = dummy

       #move R "n" places to form window of size n
       for _ in range(n):
           R = R.next
       #shift window until R is at last list element
       while R.next:
             R = R.next
             L = L.next
    
       #remove nth node now that L is at (n+1)th positon
       L.next = L.next.next

       #return head of updated list
       return dummy.next
        
    
        
