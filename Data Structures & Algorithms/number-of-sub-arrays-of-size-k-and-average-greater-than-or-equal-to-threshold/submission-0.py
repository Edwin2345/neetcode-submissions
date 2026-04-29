class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #edge case -> arr smaller than k
        if len(arr) < k:
            return 0;
        
        #slide window to get all possible subarr
        kArrCount = 0
        curSum = 0
        L = 0
        for R in range(len(arr)):
              curSum += arr[R]

              #reached size of k _. check if meet threshold and shift
              if(R - L + 1 == k):
                kArrCount += 1 if curSum/k >= threshold else 0
                curSum -= arr[L]
                L += 1
        
        return kArrCount

