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
        if(root == null){
            return 0;
        }

        return MaxDepthRec(root, 0);
    }

    public int MaxDepthRec(TreeNode curr, int currDepth){
        //if leaf, return currDepth;
        ++currDepth;
        if(curr.left == null && curr.right == null){
            return currDepth;
        }

        //Else find the max depth of the 2 subtrees
        int leftMax = 0;
        int rightMax = 0;
        if(curr.left != null){
            leftMax = MaxDepthRec(curr.left, currDepth);
        }
        if(curr.right != null){
            rightMax = MaxDepthRec(curr.right, currDepth);
        }


        //Compare and return max of 2 subtree depth
        return (leftMax > rightMax) ? leftMax : rightMax;
    }
    
}
