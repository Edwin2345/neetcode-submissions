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
    public class Tuple{
        public int depth;
        public bool isBalanced;

        public Tuple(int depth, bool isBalanced)
        {
            this.depth = depth;
            this.isBalanced = isBalanced;
        }
    }

    public bool IsBalanced(TreeNode root) {
        return DFS(root).isBalanced;
    }

    public Tuple DFS(TreeNode curr){
        //Go through every node bottom up -> DFS POST ORDER
        if(curr == null){
            return new Tuple(0, true);
        }

        Tuple leftVal = DFS(curr.left);
        Tuple rightVal = DFS(curr.right);
        
        bool isBalanced = leftVal.isBalanced && rightVal.isBalanced
                          && Math.Abs(leftVal.depth - rightVal.depth) <= 1;
        
        return new Tuple(1 + Math.Max(leftVal.depth,rightVal.depth), isBalanced);
    }

    
}
