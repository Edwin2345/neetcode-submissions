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
        oldToNew = {}
        dummy = Node(-1)
        newCur = dummy

        #copy nodes normally, adding to map
        cur = head
        while cur:
            newNode = Node(cur.val)
            oldToNew[cur] = newNode
            
            newCur.next = newNode

            cur = cur.next
            newCur = newCur.next
        
        #2nd pass: add random pointers
        cur = head
        while cur:
            if cur.random is not None:
               oldToNew[cur].random = oldToNew[cur.random]
            cur = cur.next 

        return dummy.next