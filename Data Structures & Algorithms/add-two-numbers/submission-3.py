# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    #O(M+N) time, O(1) extra space other than return list
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #create dummy ode to return nehad of new list
        dummy = ListNode()
        sumList = dummy

        remainder = 0
        while l1 or l2 or remainder > 0:
            #create new node
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sm = l1_val + l2_val + remainder

            sumList.next = ListNode(sm % 10)
            remainder = 1 if sm >= 10 else 0

            #iterate lists
            sumList = sumList.next
            if l1:
               l1 = l1.next
            if l2:
               l2 = l2.next 
             
    
        #return head of new list
        return dummy.next