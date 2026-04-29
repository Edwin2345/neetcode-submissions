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
    public bool IsSubtree(TreeNode root, TreeNode subRoot) {
        //NOT A BINARY <<SEARCH>> TREE
        if(subRoot == null){
            return true;
        }
        if(root == null){
            return false;
        }    
    
        //BFS solution --> check every node in base
        Queue<TreeNode> queue = new Queue<TreeNode>();
        queue.Enqueue(root);

        while(queue.Count > 0){
            //Process node
            TreeNode curr = queue.Dequeue();
            if(IsSameTree(curr, subRoot)){
                return true;
            }
            //Add children
            if(curr.left != null){
                queue.Enqueue(curr.left);
            }
            if(curr.right != null){
                queue.Enqueue(curr.right);
            }
        }
        return false;
    }

   
    public bool IsSameTree(TreeNode p, TreeNode q){
         //bfs this
         Queue<TreeNode> qQueue = new Queue<TreeNode>();
         Queue<TreeNode> pQueue = new Queue<TreeNode>();

         qQueue.Enqueue(q);
         pQueue.Enqueue(p);

         while(pQueue.Count > 0 || qQueue.Count > 0){
            //one queue is empty
            if(pQueue.Count == 0 ^ qQueue.Count == 0){
                return false;
            }

            //Process Nodes
            TreeNode pCurr = pQueue.Dequeue();
            TreeNode qCurr = qQueue.Dequeue();
            //pop next  if both null
            if(pCurr == null && qCurr == null){
               continue;
            }
            //check if same node
            if(pCurr == null || qCurr == null || pCurr.val != qCurr.val){
               return false;
            }


            //Add children -> including nulls
            pQueue.Enqueue(pCurr.left);
            pQueue.Enqueue(pCurr.right);
            qQueue.Enqueue(qCurr.left);
            qQueue.Enqueue(qCurr.right);
         }

         return true;
    }

}
