/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */


func reverseList(head *ListNode) *ListNode {
     //base case
	 if head == nil || head.Next == nil{
		return head
	 }

	 /*
	    1 -> 2 -> 3 ->

		newHead = 3
		2.next.next (3.next) = 2
		2.next = nil

		1.next.next = 2 
	 */

	 //recurse to last node -> thats new head
	 newHead := reverseList(head.Next)

	 //make the next pointers next point to curent node
	 head.Next.Next = head

	 //clear current next so we do't have a cycle
	 head.Next = nil

	 return newHead
}
