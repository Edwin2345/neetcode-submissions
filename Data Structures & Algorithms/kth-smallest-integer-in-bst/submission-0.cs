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
        List<int> list = new List<int>();
        InOrderTrav(root, list, k);
        return list[k-1];
    }  

    public void InOrderTrav(TreeNode node,List<int> list, int k){
        if(node == null){
            return;
        }

        InOrderTrav(node.left, list, k);

        list.Add(node.val);

        if(list.Count < k){
           InOrderTrav(node.right, list, k);
        }
    }

   
}
