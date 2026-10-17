# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #split list in half usign fast and slow points
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        head2 = slow.next
        slow.next = None

        #revese the second inked list
        cur, nxt, prev = head2, None, None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        head2 = prev

        #merge both lists back into one
        cur = head
        while head and head2:
            nxt1, nxt2 = head.next, head2.next

            cur.next = head2
            cur.next.next = nxt1
            cur = cur.next.next

            head = nxt1
            head2 = nxt2


