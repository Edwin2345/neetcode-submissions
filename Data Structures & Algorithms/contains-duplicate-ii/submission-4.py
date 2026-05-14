class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        
        #build inital fixed window up to size k+1
        #constantly check if duplicat found
        L=0
        R=0
        while R < len(nums) and R-L <= k:
            if nums[R] in window:
               return True 
            window.add(nums[R])
            R += 1
        
        #shift window to check rest
        while R < len(nums):
              #remove L, check duplicate, and add R
              window.remove(nums[L])
              if nums[R] in window:
                 return True
              window.add(nums[R])

              #shift window
              L += 1
              R += 1

        return False