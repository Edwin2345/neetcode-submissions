class DynamicArray {
public:
    int size;
    int cap;
    int* arr;

    DynamicArray(int capacity) {
       this->size=0;
       this->cap=capacity;
       this->arr = new int[capacity];
    }

    int get(int i) {
      return arr[i];
    }

    void set(int i, int n) {
       arr[i] = n;
    }

    void pushback(int n) {
      if(size == cap)
      {
        resize();
      }
      this->arr[size] = n;
      ++size;
    }

    int popback() {
      int* newArr = new int[size-1];
      int itemRemoved = arr[size-1];
      for(int i=0; i<size-1; ++i)
      {
         newArr[i] = arr[i];
      }
      delete[]arr;
      this->arr = newArr;
      newArr=NULL;
      --size;
      return itemRemoved;
    }

    void resize() {
      int* newArr = new int[cap*2];
      for(int i=0; i<size; ++i)
      {
        newArr[i] = arr[i];
      }
      delete[]arr;
      this->arr = newArr;
      this->cap = cap*2;
      newArr=NULL;
    }

    int getSize() {
      return size;
    }

    int getCapacity() {
      return cap;
    }
};
