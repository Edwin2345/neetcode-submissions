# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    #Q: is n gonna be valid? assum yes
    #P: add a dumy node and slide window to find n+1 node from end (prev)
    #P: then you can do prev.next = prev.next.next\
    # D->1->2
    #    L  R
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #insert dummy node as head to find n+1 node
        dummy = ListNode()
        dummy.next = head

        #create a window of size n
        L, R = dummy, dummy
        for _ in range(n):
            R = R.next
        
        #slide window until R is at last node (L will be n+1th node form end)
        while R.next:
            R = R.next
            L = L.next
        
        #delete the nth node
        L.next = L.next.next

        #return new head
        return dummy.next