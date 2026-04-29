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
    public int KthSmallest(TreeNode root, int k) {
        List<int> seen = new List<int>();
        DFS(root, seen, k);
        return seen[k-1];
    }

    public void DFS(TreeNode root, List<int> seen, int k){
        if(root == null){
            return;
        }

        DFS(root.left, seen, k);

        seen.Add(root.val);
        if(seen.Count == k){
            return;
        }

        DFS(root.right, seen, k);
    }

   
}
