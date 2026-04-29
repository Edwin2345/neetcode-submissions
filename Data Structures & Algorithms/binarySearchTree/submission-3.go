type TreeNode struct {
	key int
	val int
	left *TreeNode
	right *TreeNode
}

type TreeMap struct {
    root *TreeNode
}

func NewTreeMap() *TreeMap {
    return &TreeMap{root: nil}
}


func insertHelper(cur *TreeNode, k int, v int) *TreeNode{
	//base case: no node
	if cur == nil{
	   return &TreeNode{key: k, val: v}
	}

	//otherwise, build the tree by setting appropriate pointers
	if cur.key == k{
	   cur.val = v	
	} else if cur.key < k {
		cur.right = insertHelper(cur.right, k, v)
	} else {
		cur.left = insertHelper(cur.left, k, v)
	}

	return cur
}

func (tm *TreeMap) Insert(key, val int) {
     tm.root = insertHelper(tm.root, key, val)
}  

func searchFunc(cur *TreeNode, key int) int{
	if cur == nil{
       return -1
	} else if cur.key == key {
		return cur.val
	} else if cur.key < key {
		return searchFunc(cur.right, key)
	}
	return searchFunc(cur.left, key)
}

func (tm *TreeMap) Get(key int) int {
    return searchFunc(tm.root, key)
}

func (tm *TreeMap) GetMin() int {
    if tm.root == nil{
	   return -1
	}

	cur := tm.root
	for cur.left != nil{
		cur = cur.left
	}

	return cur.val
}

func (tm *TreeMap) GetMax() int {
    if tm.root == nil{
		return -1
	}

	cur := tm.root
	for cur.right != nil{
		cur = cur.right
	}
	
	return cur.val
}

func removeHelper(cur *TreeNode, key int) *TreeNode{
	//base case
	if cur == nil{
		return nil
	}

	//search for node
	if cur.key < key{
	   cur.right = removeHelper(cur.right, key)
	} else if cur.key > key {
	   cur.left = removeHelper(cur.left, key)
	//found node
	} else {
       //case 1: node is leaf, just delete
	   if cur.left == nil  && cur.right == nil{
		  return nil
       //case 2: node has only 1 child, give child to parent
	   } else if cur.left == nil {
		  return cur.right
	   } else if cur.right == nil {
		  return cur.left
	   //case 3: node has 2 children: replace with largest predecssory
	   } else {
		  predNode := cur.left
		  for predNode.right != nil{
			  predNode = predNode.right
		  }
		  
		  cur.key = predNode.key
		  cur.val = predNode.val

		  //delete pred as we copeid to current node
		  cur.left = removeHelper(cur.left, predNode.key)
	   }
	}

	return cur
}

func (tm *TreeMap) Remove(key int) {
    tm.root = removeHelper(tm.root, key)
}

func inOrderTrav(cur *TreeNode, inOrderList *[]int){
      if cur == nil{
		return
	  }

	  inOrderTrav(cur.left, inOrderList)
	  *inOrderList = append(*inOrderList, cur.key)
	  inOrderTrav(cur.right, inOrderList)
}

func (tm *TreeMap) GetInorderKeys() []int {
    inOrderList := make([]int,0)
	inOrderTrav(tm.root, &inOrderList)
    return inOrderList
}
