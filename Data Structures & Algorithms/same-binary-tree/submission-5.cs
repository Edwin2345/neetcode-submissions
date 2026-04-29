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
    public bool IsSameTree(TreeNode p, TreeNode q) {
        //BFS
        Queue<TreeNode> qQueue = new  Queue<TreeNode>();
        Queue<TreeNode> pQueue = new  Queue<TreeNode>();
        
        //Add both regardless of null
        pQueue.Enqueue(p);
        qQueue.Enqueue(q);

        while(pQueue.Count > 0 || qQueue.Count > 0){
             //Process Nodes: compare
             TreeNode pCurr = pQueue.Dequeue();
             TreeNode qCurr = qQueue.Dequeue();

             //if both null, no children to add
             if(pCurr == null && qCurr == null){
                 continue;
             }
             //false if only 1 is null, or values to add
             if(pCurr == null || qCurr == null || pCurr.val != qCurr.val){
                return false;
             }

             //Add Children from left to right (even the nulls for comparison)
             pQueue.Enqueue(pCurr.left);                     
             pQueue.Enqueue(pCurr.right);           
             qQueue.Enqueue(qCurr.left);                         
             qQueue.Enqueue(qCurr.right);            
        }

        return true;
        
    }
}
