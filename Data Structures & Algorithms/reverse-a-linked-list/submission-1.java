/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) { 
        return reverseListRec(head, null, null);
    }

    public ListNode reverseListRec(ListNode curr, ListNode next, ListNode prev)
    {
        if(curr == null)
        {
          return prev;
        }
          
        next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;

        return reverseListRec(curr, next, prev);
    }
}
