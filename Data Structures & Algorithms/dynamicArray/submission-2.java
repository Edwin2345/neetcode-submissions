class DynamicArray {

    private int[] arr;
    private int capacity;
    private int size;

    public DynamicArray(int capacity) {
       this.arr = new int[capacity];
       this.capacity = capacity;
       this.size = 0;
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if(size == capacity){
         resize();
        }
        arr[size] = n;
        ++size;
    }

    public int popback() {
        int[] newArr = new int[size-1];
        int oldBack = arr[size-1];
        for(int i=0; i<size-1; ++i){
           newArr[i] = arr[i];
        }
        this.arr = newArr;
        --size;
        return oldBack;
    }

    private void resize() {
       int[] newArr = new int[capacity*2];
       this.capacity = capacity*2;
       for(int i=0; i<size; ++i){
           newArr[i] = arr[i];
       }
       this.arr = newArr;
    }

    public int getSize() {
      return size;
    }

    public int getCapacity() {
       return capacity;
    }
}
