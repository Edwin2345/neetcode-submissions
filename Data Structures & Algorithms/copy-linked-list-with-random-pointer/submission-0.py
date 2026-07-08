"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    #P: first pass, create an old node to new node map
    #P: second pass, for each old node, 
    #     1.if old node has next. set newNode.next using map
    #     2.if old node hasrandom ptr, set new node random poitner to old random pointer new ndoe

    #O(n) time and O(n) space for map
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #base case -> empty list
        if not head:
           return None 

        #first pass, build old to new map
        oldToNewMap = {}
        cur = head
        while cur:
            oldToNewMap[cur] = Node(cur.val)
            cur = cur.next

        #second pass, set the next and random poitn if applicable
        cur = head
        while cur:
            if cur.next:
               oldToNewMap[cur].next = oldToNewMap[cur.next] 
            if cur.random:
               oldToNewMap[cur].random = oldToNewMap[cur.random] 
            cur = cur.next
            
        #return new head
        return oldToNewMap[head]
        
