# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # [1,2,4,5]
        # [9]
        # [0,3]

        Dummy = ListNode()
        sumList = Dummy
        rem = 0
        l1Cont = True
        l2Cont = True
        while( l1Cont or l2Cont or rem > 0):
            #create new node
            nodeVal = (l1.val + l2.val + rem) % 10
            rem = (l1.val + l2.val + rem) // 10
            sumList.next = ListNode(nodeVal)
            sumList = sumList.next

            #iterate l1 as long as not at end
            if(l1.next is None):
                l1Cont = False
                l1.val = 0
            else:
                l1 = l1.next
            
            #iterate l2 as long as not at end
            if(l2.next is None):
                l2Cont = False
                l2.val = 0
            else:
                l2 = l2.next
            
        return Dummy.next