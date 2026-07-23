"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
   
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {}

        def copyRec(cur):
            #base case
            if not cur:
               return None

            #copy node and put in map
            newNode = Node(cur.val)
            oldToNew[cur] = newNode

            #recurse to build next node
            copyRec(cur.next)

            #set next and random pointers
            newNode.next = oldToNew[cur.next] if cur.next else None
            newNode.random = oldToNew[cur.random] if cur.random else None
            
            return newNode 
        

        return copyRec(head)