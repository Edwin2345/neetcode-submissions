# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode();
        curr = dummyHead

        while( list1 and list2 ):
            if(list1.val < list2.val):
               curr.next = list1
               list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        #copy over the remaining
        if(list1 is not None):
            curr.next = list1
        elif(list2 is not None):
            curr.next = list2

        return dummyHead.next