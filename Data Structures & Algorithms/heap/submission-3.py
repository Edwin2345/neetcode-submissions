class MinHeap:
    
    def __init__(self):
        #0th index should be dummy
        self._arr = [-1]

    def push(self, val: int) -> None:
        #insert at end of arr
        self._arr.append(val)
        i = len(self._arr)-1
        #percolate up -> swap parent with curr if parent larger
        p = i // 2
        while(p > 0 and self._arr[p] > self._arr[i]):
            self._arr[p],self._arr[i] = self._arr[i],self._arr[p]
            i = p
            p = i // 2
    
    #helper function to swap parent with child if parent larger
    def percolate_down(self, i):
        #iterate while left child is still in bound
        while(True):  
            #index of left and right children
            L = 2*i
            R = 2*i + 1   

            #swap with right child with parent if its smaller than both parent and left
            if R < len(self._arr) and self._arr[R] < self._arr[i] and self._arr[R] < self._arr[L]:
                self._arr[R],self._arr[i] = self._arr[i],self._arr[R]
                i = R
            #else, swap with left child
            elif L < len(self._arr) and self._arr[L] < self._arr[i]:
                self._arr[L],self._arr[i] = self._arr[i],self._arr[L] 
                i = L       
            #parent larger than chidren -> valid heap
            else:
                return

    def pop(self) -> int:
        #edge cases -> zero or 1 element in heap
        if len(self._arr) == 1:
           return -1
        if len(self._arr) == 2:
            return self._arr.pop()

        #insert last element in 1st position, and then percolate down
        minVal = self._arr[1]
        self._arr[1] = self._arr.pop()
        self.percolate_down(1)   
        return minVal
        

    def top(self) -> int:
        #edge case -> empty heap
        if len(self._arr) == 1:
            return -1
        #otherwise return top
        return self._arr[1]
        

    def heapify(self, nums: List[int]):
        #edge case -> empty nums
        if not nums:
            return

        #push first element to end as index 0 not used
        nums.append(nums[0])
        self._arr = nums
        
        #percolate down from all the nodes with children
        i = len(self._arr)-1
        while(i > 0):
            self.percolate_down(i)
            i -= 1


        
        