"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    #P: do this in two passes -> 1st pass, copy the nodes themselfs
    #P: create a map called oldToNew, that will bap the old pointer to the newly created ndoe
    #P: second pass fill in the random pointers with 
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #base case: empty list
        if not head:
           return head 

        oldToNew = {}

        #1st pass: create new nodes with correct values and add to map
        cur = head
        while cur:
            oldToNew[cur] =  Node(cur.val)
            cur = cur.next
        
        #2nd pass: add next and random pointers
        cur = head
        while cur:
            if cur.next is not None:
               oldToNew[cur].next = oldToNew[cur.next] 
            if cur.random is not None:
               oldToNew[cur].random = oldToNew[cur.random]
            cur = cur.next 

        return oldToNew[head]