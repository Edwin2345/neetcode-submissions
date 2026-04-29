# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currPtr = head
        prevPtr = None
        nextPtr = None

        while(currPtr != None):
            nextPtr = currPtr.next
            currPtr.next = prevPtr
            prevPtr = currPtr
            currPtr = nextPtr


        return prevPtr