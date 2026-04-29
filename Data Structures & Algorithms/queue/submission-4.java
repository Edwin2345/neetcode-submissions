class Deque {

    class Node{
        public int val;
        public Node next;
        public Node prev;
        
        public Node(int val){
           this.val = val;
           this.next = null;
           this.prev = null;
        }
    }

    private Node head;
    private Node tail;

    public Deque() {
       this.head = null;
       this.tail = null;
    }

    public boolean isEmpty() {
       return head == null;
    }

    public void append(int value) {
       if(isEmpty()){
         head = new Node(value);
         tail = head;
       } 
       else{
          tail.next = new Node(value);
          tail.next.prev = tail;
          tail = tail.next;
       }      
    }

    public void appendleft(int value) {
        Node newHead = new Node(value);
        if(isEmpty()){
            head = newHead;
            tail = newHead;
        }
        else{
            newHead.next = head;
            head.prev = newHead;
            head = newHead;
        }
    }

    public int pop() {
        if(isEmpty()){
            return -1;
        }

        int val = tail.val;
        if(head == tail){
            head = null;
            tail = null;
        }  
        else{
            tail = tail.prev;
            tail.next = null;
        }
        return val;
    }  

    public int popleft() {
        if(isEmpty()){
          return -1;
        }
        
        int val = head.val;
        if(head == tail){
           pop();
        }
        else{
            head = head.next;
            head.prev = null;
        }
        return val;
    }
}
