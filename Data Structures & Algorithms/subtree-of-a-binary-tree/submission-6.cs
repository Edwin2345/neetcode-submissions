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
        if(p == null && q == null){
            return true;
        }

        if(p == null || q == null || (p.val != q.val)){
            return false;
        }

        return IsSameTree(p.left, q.left) && IsSameTree(p.right, q.right);
    }

}
