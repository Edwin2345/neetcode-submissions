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
    public List<int> RightSideView(TreeNode root) {
        List<int> ans = new List<int>();
       
        //BFS but start right and take whats possible
        Queue<TreeNode> queue = new Queue<TreeNode>();

        if(root != null){
            queue.Enqueue(root);
        }

        while(queue.Count > 0){
            //Reset right side every level
            int levelLenght = queue.Count;
            bool rightSideFound = false;
            
            for(int i=0; i<levelLenght; ++i){
                //Process current node -> take first 1 to be right side
                TreeNode curr = queue.Dequeue();
                if( !rightSideFound ){
                   rightSideFound = true;
                   ans.Add(curr.val);
                }

                //Add Children right to left
                if(curr.right != null){
                    queue.Enqueue(curr.right);
                }
                if(curr.left != null){
                    queue.Enqueue(curr.left);
                }
            }
        }

        return ans;
    }
}
