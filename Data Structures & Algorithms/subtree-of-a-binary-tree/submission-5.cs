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
        
        //Vacuous Case
        if(subRoot == null){
           return true;
        }

        //Reached the end of Base Tree
        if(root == null){
            return false;
        }

       
        //DFS PREORDER -> check on every node if same tree as subtree
        //######
        if(IsSameTree(root, subRoot)){
            return true;
        }

        return IsSubtree(root.left, subRoot) || IsSubtree(root.right, subRoot);
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
