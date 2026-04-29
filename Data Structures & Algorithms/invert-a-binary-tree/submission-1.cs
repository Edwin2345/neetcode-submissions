/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    public TreeNode InvertTree(TreeNode root) {
           //DFS ITERATIVE PREORDER
           //#############

           TreeNode curr = root;
           Stack<TreeNode> stack = new Stack<TreeNode>();

           while(curr != null || stack.Count > 0){
               if(curr != null){
                   //Process Node -> Swap
                   TreeNode temp = curr.left;
                   curr.left = curr.right;
                   curr.right = temp;

                   //Add Right node to stack, go left
                   if(curr.right != null){
                      stack.Push(curr.right);
                   }
                   curr = curr.left;
               }
               else{
                    //go back to right SB
                    curr = stack.Pop();
               }
           }

           return root;
    }
}
