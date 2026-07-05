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
        
        #otherwise, retiur the smaller one, but set next pointer recursively
        if list1.val < list2.val:
           node = list1
           node.next = self.mergeTwoLists(list1.next, list2)
           return node
        else:
           node = list2
           node.next = self.mergeTwoLists(list1, list2.next)
           return node