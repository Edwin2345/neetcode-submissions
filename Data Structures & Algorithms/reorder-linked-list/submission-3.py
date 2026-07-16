# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
      #place into a list we can index
      nodeList = []
      cur = head
      while cur:
         nodeList.append(cur)
         cur = cur.next
       
      #reorder
      i = 0
      j = len(nodeList) - 1
      while i < j:
         nodeList[i].next = nodeList[j]
         i += 1
         if i == j:
            break
         nodeList[j].next = nodeList[i]
         j -= 1
      
      #last node need to point to none, else cycle
      nodeList[i].next = None