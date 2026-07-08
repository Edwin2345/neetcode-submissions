# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #base case
        if not head:
           return None

        #store nodes in a list
        nodeList = []
        cur = head
        while cur:
           nodeList.append(cur)
           cur = cur.next
        
        #reverse list
        L, R = 0, len(nodeList)-1
        while L < R:
            nodeList[L].next = nodeList[R]
            L += 1
            if L == R:
               break
            nodeList[R].next = nodeList[L]
            R -= 1
         
        nodeList[L].next = None



      