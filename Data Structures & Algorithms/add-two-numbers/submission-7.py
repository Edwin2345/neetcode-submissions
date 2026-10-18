# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #dummy node for sum list
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or (carry > 0):
            #null coalese list value
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            #create new sum node
            sm = l1Val + l2Val + carry 
            cur.next = ListNode( sm % 10 )
            carry = sm // 10

            #iterate to next pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next

        return dummy.next