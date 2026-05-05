/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }


Questions
1. will we ever get an empty or single node tree

Approach -> one of the dfs algos
         -> return if current node is nul
		 -> swap Left child wtih Right chiuld
		 -> recurse Left or Right
		 -> time: o(n) -> where number of nodes is n
		 -> space: constant time, o(n) for call stack
 */

func invertTree(root *TreeNode) *TreeNode { 
	 //base case -> null tree
	 if root == nil{
		return nil
	 }

     //swap current node children
	 tmpNode := root.Right
	 root.Right = root.Left
	 root.Left = tmpNode

     //recurse to children
	 invertTree(root.Left)
     invertTree(root.Right)
     
	 //return inverted tree
	 return root
}
