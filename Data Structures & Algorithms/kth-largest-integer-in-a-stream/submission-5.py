class KthLargest:
    #bucket sort -> O(N)
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.buckets = [0]*2001
        for n in nums:
            self.buckets[1000-n] += 1

    #add is O(n)
    def add(self, val: int) -> int:
        self.buckets[1000-val] += 1

        foundCnt = 0
        for i in range(2001):
            cnt = self.buckets[i] 
            while cnt > 0:
                foundCnt += 1
                if foundCnt == self.k:
                   return 1000-i 
                cnt -= 1
    

     
        
