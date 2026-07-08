# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    #O(N) time, O(1) space
    def reorderList(self, head: Optional[ListNode]) -> None:
      #find mid poitn of list using fast and slow ptrs
      mid, fast = head, head
      while fast and fast.next:
         fast = fast.next.next
         mid = mid.next
      
      #split the list at the midpoint (1st haf inlcudes midpoint)
      secondHead = mid.next
      mid.next = None
         
      #reverse the 2nd half of list (from mid to end)
      #at the end prev is the head of reversed half
      #[0->1->2->3->4->5->6] --> [0->1->2->3] [4<-5<-6]
      cur,prev,nxt = secondHead,None,None
      while cur:
         nxt = cur.next
         cur.next = prev
         prev = cur
         cur = nxt
      
      #merge two lists together
      #[0->1->2->3->4->5->6] --> [0->1->2->3] [4<-5<-6]
      fwd = head
      rev = prev
      while rev:
         #save the next nodes in both halfs
         nxtNode = fwd.next
         nxtRevNode = rev.next

         #insert the reverse inbetween fwd and next fwd
         fwd.next = rev
         rev.next = nxtNode
        
         #iterate to next fwd
         fwd = nxtNode
         rev = nxtRevNode


      