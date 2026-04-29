# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rec(self, head, n):
        #reached end of LL
        if(head is None):
            return None
        
        #recurse through list, setting next pointer
        head.next = self.rec(head.next,n)
        #once end of list reached, beging decrementing count to find target
        n[0] -= 1
        if(n[0] == 0):
            #target node found, ensure it gets skipped
            return head.next
        return head


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
         1 -> 2 -> 3 -> 4 -> None
        '''
        return self.rec(head,[n])

