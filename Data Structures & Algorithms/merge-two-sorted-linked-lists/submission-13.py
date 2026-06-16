# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:    
        #dummy node for head of new list
        dummy = ListNode()  
        tmp = dummy
        while list1 and list2:
            #add the smaller node and shift list
            if list1.val < list2.val:
               tmp.next = list1
               list1 = list1.next
            else:
               tmp.next = list2
               list2 = list2.next
            
            #shift the new list
            tmp = tmp.next
        
        #only 1 list left, append entire list
        if list1:
           tmp.next = list1 
        elif list2:
           tmp.next = list2


        #return head of new list
        return dummy.next
    