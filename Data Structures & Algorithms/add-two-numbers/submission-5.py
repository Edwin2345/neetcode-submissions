# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #dummy node
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            #convert null values to 0
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            #compute sum and create new node + carry
            sm = l1_val + l2_val + carry
            cur.next = ListNode(sm % 10)
            carry = 1 if sm >= 10 else 0

            #move pointers
            if l1:
               l1 = l1.next
            if l2:
               l2 = l2.next
            cur = cur.next  
        
        return dummy.next