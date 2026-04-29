public class MinStack {

    public List<int> stack;
    public List<int> minStack;

    public MinStack() {
        this.stack = new List<int>();
        this.minStack =  new List<int>();
    }
    
    public void Push(int val) {
        stack.Add(val);
        if(minStack.Count == 0){
            minStack.Add(val);
        }
        else if(val < minStack[minStack.Count-1]){
            minStack.Add(val);
        }
        else{
            minStack.Add(minStack[minStack.Count-1]);
        }
    }
    
    public void Pop() {
        stack.RemoveAt(stack.Count-1);
        minStack.RemoveAt(minStack.Count-1);
    }
    
    public int Top() {
        return stack[stack.Count-1];
    }
    
    public int GetMin() {
        return minStack[minStack.Count-1];
    }
}
