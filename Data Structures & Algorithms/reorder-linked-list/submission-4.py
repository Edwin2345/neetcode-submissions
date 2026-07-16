# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find midpoint of list and then split into first and second list
        slowPtr, fastPtr = head, head
        while fastPtr and fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        secondHead = slowPtr.next
        slowPtr.next = None

        # reverse the second list
        prev, cur, nxt = None, secondHead, None
        while cur != None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        secondHead = prev

        #merge the 1st list with 2nd list
        while head and secondHead:
            firstListNxt = head.next
            secondListNxt = secondHead.next

            head.next = secondHead
            secondHead.next = firstListNxt

            head = firstListNxt
            secondHead = secondListNxt

