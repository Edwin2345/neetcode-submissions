class MinStack {
    public Node topNode; 
    public int  min=0;
    public int length=0;
  
    public MinStack() {

    }
    
    public void push(int val) {
        if(topNode == null){
           topNode = new Node(val);
           min = val;
        }
        else{
           Node tempNode = topNode;
           topNode.next = new Node(val);
           topNode = topNode.next;
           topNode.prev = tempNode;

           if(val < min){
            min = val;
           }
        }
        ++length;
    }
    
    public void pop() {
        if(topNode.prev == null){
            topNode = null;
        }
        else
        {
            topNode = topNode.prev;
            min = topNode.val;
            Node tempNode = topNode;
            while(tempNode != null)
            {
                if(tempNode.val < min)
                {
                    min = tempNode.val;
                }
                tempNode = tempNode.prev;
            }
        }

        --length;
    }
    
    public int top() {
        return topNode.val;
    }
    
    public int getMin() {
        return min;
    }
}

class Node{
    public Node next;
    public Node prev;
    public int val;

    public Node(int val){
        this.next = null;
        this.prev = null;
        this.val = val;
    }
}
