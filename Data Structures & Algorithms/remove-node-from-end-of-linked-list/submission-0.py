# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newHead = None
        #[1,2,3,4,5]
        # build an array of nodes
        nodes = []
        tmp = head
        while tmp is not None:
            nodes.append(tmp)
            tmp = tmp.next
        L = len(nodes)

        #removing begining of list
        if(n == L and head is not None):
            newHead = head.next
        #remove end of list
        elif(n == 1):
            nodes[L-2].next = None
            newHead = nodes[0]
        #remove from middle
        else:
            #set previous node to next node
            nodes[L-n-1].next = nodes[L-n+1]
            newHead = nodes[0]
        return newHead
