/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseListRec(prev *ListNode, cur *ListNode, next *ListNode) *ListNode{
	//done reversing
	if cur == nil{
	   return prev
	}

	next = cur.Next
	cur.Next = prev
	prev =  cur
	cur = next

    return reverseListRec(prev, cur, next)
} 

func reverseList(head *ListNode) *ListNode {
     return reverseListRec(nil, head, nil)
}
