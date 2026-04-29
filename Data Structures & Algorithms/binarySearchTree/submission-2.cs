class TreeMap {
    public class TreeNode{
        public int key;
        public int val;
        public TreeNode left;
        public TreeNode right;

        public TreeNode(int key, int val){
            this.key = key;
            this.val = val;
        }
    }

    public TreeNode root;

    public TreeMap() {
      this.root = null;
    }

    public void Insert(int key, int val) {
        TreeNode InsertNode(TreeNode curr, int k, int v){
             //Create or update target value node
             if(curr == null){
                return new TreeNode(k, v);
             }
             else if(k == curr.key){
                curr.val = v;
                return curr;
             }

             //Set Children
             else if(k < curr.key){
                curr.left = InsertNode(curr.left, k, v);
             }
             else{
                curr.right = InsertNode(curr.right, k, v); 
             }

             return curr;
        }

        this.root = InsertNode(root, key, val);
    }

    public int Get(int key) {
        int Search(TreeNode curr, int k){
            if(curr == null){
                return -1;
            }
            else if(k == curr.key){
                return curr.val;
            }
            else if(k > curr.key){
                return Search(curr.right, k);
            }
            return Search(curr.left, k);
        }

        return Search(root, key);
    }

    public int GetMin() {
        if(root == null){
            return -1;
        }

        TreeNode curr = root;
        while(curr.left != null){
            curr = curr.left;
        }

        return curr.val;
    }


    public int GetMax() {
        if(root == null){
            return -1;
        }

        TreeNode curr = root;
        while(curr.right != null){
            curr = curr.right;
        }

        return curr.val;
    }


    public void Remove(int key) {
        TreeNode GetMinNode(TreeNode root){
            if(root == null){
              return null;
            }
             
            while(root.left != null){
               root = root.left;
            }

            return root;
        }

        TreeNode RemoveNode(TreeNode curr, int k){
            if(curr == null){
                return null;
            }
            else if(k > curr.key){
                curr.right = RemoveNode(curr.right, k);
            }
            else if(k < curr.key){
                curr.left = RemoveNode(curr.left, k);
            }
            //Found the node
            else{
                //1 or 0 children -> bring them up
                if(curr.right == null){
                    return curr.left;
                }
                if(curr.left == null){
                    return curr.right;
                }

                //2 children
                //Replace with key/value of smallest node greater
                TreeNode smallestNodeGreater = GetMinNode(curr.right);
                curr.key = smallestNodeGreater.key;
                curr.val = smallestNodeGreater.val;

                //delete the smallest node greater node from right
                curr.right = RemoveNode(curr.right, smallestNodeGreater.key);
            }

            return curr;
        } 

        this.root = RemoveNode(root, key);
    }


    public List<int> GetInorderKeys() {
        List<int> ans = new List<int>();

        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode curr = root;

        while(curr != null || stack.Count > 0){
             if(curr != null){
                //go as far left, while adding curr node to stack
                stack.Push(curr);
                curr = curr.left;
             }
             else{
                //Pop from stack and process, go right
                curr = stack.Pop();
                ans.Add(curr.key);
                curr = curr.right;
             }
        }
        
        return ans;
    }

}
