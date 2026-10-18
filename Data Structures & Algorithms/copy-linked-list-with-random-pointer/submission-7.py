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
        #base case --> empty list
        if head is None:
           return None
            
        #map old ndoes to there new copies
        oldToNew = {}

        #one pass to shallow copy nodes
        cur = head
        while cur is not None:
            oldToNew[cur] = Node(cur.val)
            cur = cur.next
        
        #one pass to set next and cur pointers
        cur = head
        while cur is not None:
            if cur.next is not None:
               oldToNew[cur].next = oldToNew[cur.next]
            if cur.random is not None:
               oldToNew[cur].random = oldToNew[cur.random]  
            cur = cur.next
        
        return oldToNew[head] 