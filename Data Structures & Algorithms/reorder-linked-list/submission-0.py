# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    #O(N) Time, O(N) Space
    def reorderList(self, head: Optional[ListNode]) -> None:
        #base case
        if not head:
           return None 

        #add nodes to an array
        nodeList = []
        cur = head
        while cur:
           nodeList.append(cur)
           cur = cur.next
        
        #reorder list
        L,R = 0,len(nodeList)-1
        while L < R:
            #leftNode points to ndoe at end
            nodeList[L].next = nodeList[R]
            L += 1

            #reached one half
            if L >= R:
               break 
            
            #right ndoe points to next left
            nodeList[R].next = nodeList[L]
            R -= 1
        
        #last left node is now tail (middle or last pair), must point to nothing
        nodeList[L].next = None

     

 
                
        