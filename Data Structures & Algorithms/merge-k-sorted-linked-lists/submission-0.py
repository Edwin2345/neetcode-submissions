# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   
    #idea: keep pointers to each of the k smallest lists and add (val, pointer) to min_heap
    #pop smalelst from min ehap, and add back its next value
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #create merged list
        mergedList = ListNode()
        cur = mergedList

        #have a counter variable to ensure heapify will only run on numbers
        counter = 0
        
        #add every list's head to min heap
        min_heap = []
        for head in lists:
            counter += 1
            if not head:   
               continue            
            min_heap.append( (head.val, counter, head) )
        heapq.heapify(min_heap)
         
        while len(min_heap) > 0:
            #get the smallest value node
            _, _, node = heapq.heappop(min_heap)
            cur.next = node
            cur = cur.next

            #add the next node of that list to the heap
            counter += 1
            if node.next:
               node = node.next
               heapq.heappush(min_heap, (node.val, counter, node))
        
        #return head of the meged list
        return mergedList.next





        