# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        D -> 1 -> 2 -> 3 -> 4 -> None
        '''
        
        #Add a dummy node -> offset window by -1
        Dummy = ListNode()
        Dummy.next = head

        #create sliding window starting from dummy
        L=R=Dummy
        for i in range(n):
            R = R.next
        
        #shift sliding window to end (None)
        while(R.next is not None):
            R = R.next
            L = L.next

        L.next = L.next.next

        return Dummy.next