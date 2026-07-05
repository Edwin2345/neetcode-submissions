# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    #use fast poitner that goes nex.next and slow ptr that jsut gos next
    #the place where fast point adn slow point inercet is where cycle is
    #if they both exit, not cycle
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowPtr = head
        fastPtr = head

        while fastPtr and fastPtr.next:
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next
            if slowPtr == fastPtr:
               return True 

        return False