class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        validSubarrays = []
        curSum = 0

        L,R = 0,0
        while R < len(arr):
            #shrink window until we are able to add R
            while R-L+1 > k:
                curSum -= arr[L]
                L += 1
            
            #add R, and see if valid subarray thta meets threshodl
            curSum += arr[R]
            if R-L+1 == k and curSum / k >= threshold:
               validSubarrays.append( arr[L:R+1] )

            R += 1 
        
       # print(validSubarrays)
        return len(validSubarrays)