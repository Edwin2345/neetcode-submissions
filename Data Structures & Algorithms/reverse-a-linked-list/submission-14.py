# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#   a -> b -> c
# p c    n
class Solution:
    #P: Recursive solutuon: helper with (node,prev)
    #P: If not ndoe, return prev (that way last call will return tail)
    #P: save next, and make node.next point at prev
    #P: return the next funciton call so base case will return tail
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(node, prev):
            if not node:
               return prev
            nextNode = node.next
            node.next = prev
            return rev(nextNode, node) 

        return rev(head, None)

              