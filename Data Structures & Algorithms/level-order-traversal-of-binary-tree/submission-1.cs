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
    public List<List<int>> LevelOrder(TreeNode root) {
        List<List<int>> ans = new List<List<int>>();
        Queue<TreeNode> queue = new Queue<TreeNode>();

        //Attach Root
        if(root != null){
            queue.Enqueue(root);
        }

        //Continue until all nodes traverst
        while( queue.Count > 0 ){

            //Get current Level Size 
            int levelSize = queue.Count;
            List<int> row = new List<int>();

            //Iterate for that level
            for(int levelIndex=0; levelIndex < levelSize; ++levelIndex){
                //process node
                TreeNode curr = queue.Dequeue();
                row.Add(curr.val);

                //Add Children
                if(curr.left != null){
                    queue.Enqueue(curr.left);
                }
                if(curr.right != null){
                    queue.Enqueue(curr.right);
                }
            }

            ans.Add(row);
        }

        return ans;
    }
}
