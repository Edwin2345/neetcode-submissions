# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #base cases
        if not list1:
           return list2
        if not list2:
           return list1

        #create dummy to start merged list
        dummy = ListNode()
        cur = dummy

        #keep on taking smallest while both nodes present
        while list1 and list2:
            if list1.val < list2.val:
               cur.next = list1
               list1 = list1.next
            else:
               cur.next = list2
               list2 = list2.next
            cur = cur.next
        
        #append non null list if applciable
        if list1:
           cur.next = list1
        if list2:
           cur.next = list2 

        return dummy.next
         