# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    #pairwise merging -> merg pairs of 2 lists, then merg those merged pairs
    #repet unilt only 1 list left (divided number of lsits by 2 each time)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #base case, no lists
        if len(lists) == 0:
           return None 
        
        #helper funciton to merge 2 lists
        def mergeTwoLists(l1, l2):
            dummy = ListNode()
            cur = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                   cur.next = l1
                   l1 = l1.next
                else:
                   cur.next = l2
                   l2 = l2.next
                cur = cur.next

            if l2:
               cur.next = l2
            if l1:
               cur.next = l1 

            return dummy.next  
        
        #pairwise merge
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append( mergeTwoLists(list1, list2) )
            lists = mergedLists
                
        #return the final merged list
        return lists[0]