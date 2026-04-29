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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(-100);
        ListNode temp = dummy;
        mergeTwoListRec(temp, list1, list2);
        return dummy.next;
    }        

    public void mergeTwoListRec(ListNode temp, ListNode list1, ListNode list2){
        if(list1 == null){
            temp.next = list2;
            return;
        }
        else if(list2 == null){
            temp.next = list1;
            return;
        }

        if(list1.val < list2.val){
            temp.next = list1;
            list1 = list1.next;
        }
        else{
            temp.next = list2;
            list2 = list2.next;
        }

        temp = temp.next;
        mergeTwoListRec(temp, list1, list2);
    }
}