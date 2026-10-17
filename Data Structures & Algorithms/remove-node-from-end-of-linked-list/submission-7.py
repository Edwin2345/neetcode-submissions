# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    #to remove the nth node, we need to be at n-1th node
    #CONSTRAINTS: n is always valid for list
    #  D -> 1 -> 2 ->
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:        
        #insert a dummy node at the head to get windowto wokrd
        dummy = ListNode()
        dummy.next = head

        #use two pointers to create a window of size n
        L,R = dummy, dummy
        for i in range(n):
            R = R.next
        
        #shift this window until R is at end of linked list
        while R and R.next:
            R = R.next
            L = L.next
        
        #Remove node and return new head
        L.next = L.next.next
        return dummy.next