class KthLargest:
    # O(N)
    def __init__(self, k: int, nums: List[int]):
        self.bucket = [0]*2001
        self.k = k

        for n in nums:
            # -1000 --> 0
            # -999 --> 1
            # 0 --> 1000
          # 1000 --> 2000
            self.bucket[n + 1000] += 1
       
    # O(N-k)
    def add(self, val: int) -> int:
        #add to bucket
         self.bucket[val + 1000] += 1

         #search backwards to find kth largest
         cnt = 0
         for i in range(2000, -1, -1):
             cnt += self.bucket[i]
             if cnt >= self.k:
                return i - 1000
        
