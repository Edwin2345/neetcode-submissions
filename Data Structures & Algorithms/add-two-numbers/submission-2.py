# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    #P: while both lsit have values
    #    --> add 2 ndoex + remainder and take mod 10 to get ans node val
    #    --> carry the remainder for next
    #P: if only 1 list has values
    #    --> add remainder to ndoe val, mod 10 carry to next    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #create dummy ode to return nehad of new list
        dummy = ListNode()
        sumList = dummy

        #sum both lists while both exist
        remainder = 0
        while l1 and l2:
            #add new sum node
            res = l1.val + l2.val + remainder
            sumList.next = ListNode(res%10)
            remainder = 1 if res >= 10 else 0

            #iterate all to next node
            l1 = l1.next
            l2 = l2.next
            sumList = sumList.next
        
        #if only 1 list remains, add next digits with any remainder left
        remList = l1 if l1 else l2
        while remList:
            res = remList.val + remainder
            sumList.next = ListNode(res%10)
            remainder = 1 if res >= 10 else 0

            remList = remList.next
            sumList = sumList.next
        
        #create new node if remainder remains
        if remainder == 1:
           sumList.next = ListNode(1) 

        #return nehad of new list
        return dummy.next