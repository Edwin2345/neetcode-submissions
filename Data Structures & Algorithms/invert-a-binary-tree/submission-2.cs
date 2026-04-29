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
           //BFS
           //#############
           Queue<TreeNode> queue = new Queue<TreeNode>();
           if(root != null){
             queue.Enqueue(root);
           }

           while(queue.Count > 0){
               //process node -> swap
               TreeNode curr = queue.Dequeue();
               TreeNode temp = curr.left;
               curr.left = curr.right;
               curr.right = temp;
               
               //Add Children
               if(curr.left != null){
                  queue.Enqueue(curr.left);
               }
               if(curr.right != null){
                  queue.Enqueue(curr.right);
               }
           }

           return root;
    }
}
