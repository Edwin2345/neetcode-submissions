# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbersRec(self, l1, l2, carry):
        #base case
        if not l1 and not l2 and carry == 0:
           return None

        #compute sum
        l1Val = l1.val if l1 else 0
        l2Val = l2.val if l2 else 0
        sm = l1Val + l2Val + carry

        #create new node and update carry
        node = ListNode(sm%10)
        carry = 1 if sm >= 10 else 0

        #recursively set next node 
        l1Next = l1.next if l1 else None
        l2Next = l2.next if l2 else None
        node.next = self.addTwoNumbersRec(l1Next, l2Next, carry)
       
        return node


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.addTwoNumbersRec(l1, l2, 0)