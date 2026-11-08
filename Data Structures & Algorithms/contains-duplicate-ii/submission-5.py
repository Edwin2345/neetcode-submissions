class Solution:
    #use a fixed widnow of size k and a set to check for duplicates in range
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        windowMap = {}
        L,R = 0,0
        while R < len(nums):
            #shrink window until able to add R
            while R-L > k:
                del windowMap[nums[L]]
                L += 1
            
            #add R, check for duplicates
            if nums[R] in windowMap:
               print("value: " + str(nums[R]))
               print("indices: " + str([R, windowMap[nums[R]]]))
               return True
            windowMap[nums[R]] = R
            R += 1

        #no duplicates in widnow found
        return False 
        