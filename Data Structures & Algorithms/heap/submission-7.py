class MinHeap:
    
    def __init__(self):
        self.heap = [-1]
        

    def push(self, val: int) -> None:
        #insert new val at end of heap
        self.heap.append(val)

        #percolate the value upwards -> swap parent with child if child larger
        i = len(self.heap) - 1
        parentIndex = i//2
        while(parentIndex > 0 and self.heap[parentIndex] > self.heap[i]):
            self.heap[parentIndex],self.heap[i] = self.heap[i],self.heap[parentIndex]
            i = parentIndex
            parentIndex = i//2
    
    def percolate_down(self, i):
        #get indices of left and right children
        left = 2*i
        right = 2*i + 1

        #keep on swaping parent with the min of children if smaller
        while(left < len(self.heap)):
            #swap current with right child
            if(right < len(self.heap) and self.heap[right] < self.heap[i] and self.heap[right] < self.heap[left]):
                self.heap[right],self.heap[i] = self.heap[i],self.heap[right]
                i = right
            #swap current with left child
            elif(self.heap[left] < self.heap[i]):
                self.heap[left],self.heap[i] = self.heap[i],self.heap[left]
                i = left
            #no swaps needed -> heap order properity is good
            else:
                break
            
            #recompute child indixes
            left = 2*i
            right = 2*i + 1



    def pop(self) -> int:
        #empty heap
        if len(self.heap) <= 1:
            return -1
        
        #pop by replacing top element with last
        minVal = self.heap[1]
        self.heap[1] = self.heap[len(self.heap)-1]
        self.heap.pop()

        #fix heap order property using percolate function
        self.percolate_down(1)

        return minVal
        

    def top(self) -> int:
        #empty heap
        if len(self.heap) == 1:
            return -1
        return self.heap[1]
        

    def heapify(self, nums: List[int]) -> None:
        #edge case -> empty heap
        if not nums:
           self.heap = nums
           return

        #move the index 0 element to end as index 0 must be unsued
        nums.append(nums[0])
        self.heap = nums

        #starting from end of heap -> percolate down to get order property
        for i in range(len(self.heap)-1,0,-1):
            self.percolate_down(i)
        
        