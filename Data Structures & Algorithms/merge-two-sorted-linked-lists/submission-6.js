/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */

    mergeTwoListsRec(temp, list1, list2) {
        if(list1 == null && list2 == null){
            return;
        }
        else if(list1 != null && list2 == null){
            temp.next = list1;
            return;
        }
        else if(list2 != null && list1 == null){
            temp.next = list2;
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

        return this.mergeTwoListsRec(temp.next, list1, list2)
    }

    mergeTwoLists(list1, list2){
        const dummy = new ListNode();
        let temp  = dummy;
        this.mergeTwoListsRec(temp, list1, list2);
        return dummy.next;
    }
}
