# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fastPtr, slowPtr = head, head

        while fastPtr and fastPtr.next:
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next

            if slowPtr == fastPtr:
               return True 
        

        return False