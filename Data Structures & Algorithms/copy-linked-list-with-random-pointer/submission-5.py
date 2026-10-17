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
        def deepCopy(node):
            #base case
            if node is None:
               return None

            #shallow copy curent node and add it to Map
            oldToNew[node] = Node(node.val)

            #copy its new and random pointers recursively
            oldToNew[node].next = deepCopy(node.next)
            if node.random is not None:
               oldToNew[node].random = oldToNew[node.random] 
            
            return oldToNew[node]
        
        return deepCopy(head)
        