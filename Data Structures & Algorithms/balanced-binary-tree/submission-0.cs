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
    public bool IsBalanced(TreeNode root) {
        //Go through every node
        //check if depth of every node is < +/- 1
        if(root == null){
          return true;
        }

        int diff = Depth(root.left) - Depth(root.right);
        if( diff > 1 || diff < -1 ){
            return false;
        }

        return IsBalanced(root.left) && IsBalanced(root.right);
    }

    public int Depth(TreeNode curr){
        if(curr == null){
            return 0;
        }

        return 1 + Math.Max( Depth(curr.left), Depth(curr.right) ); 
    }
}
