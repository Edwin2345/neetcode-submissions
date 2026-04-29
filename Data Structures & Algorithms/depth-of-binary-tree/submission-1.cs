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
    public int MaxDepth(TreeNode root) {
        //BFS
        int depth = 0;
        Queue<TreeNode> queue = new Queue<TreeNode>();
        
        if(root != null){
            queue.Enqueue(root);
        }

        while(queue.Count > 0){
            ++depth;
            int levelLength = queue.Count;

            for(int i=0; i<levelLength; ++i){
                //Process Node
                TreeNode curr = queue.Dequeue();                

                //Add Children
                if(curr.left != null){
                    queue.Enqueue(curr.left);
                }
                if(curr.right != null){
                    queue.Enqueue(curr.right);
                }
            }        
        }
  
        return depth;
    }

   
}
