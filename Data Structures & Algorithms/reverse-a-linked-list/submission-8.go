/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseList(head *ListNode) *ListNode {
    //set all pointers
    curr := head
	var prev *ListNode = nil
    var next *ListNode = nil

	/*
	   A -> B -> C
	   next = curr.next
	   curr.next = prev
	   prev = curr
	   curr = next
	*/
	for curr != nil{
        next = curr.Next
		curr.Next = prev
		prev = curr
		curr = next
	}

	return prev
}
