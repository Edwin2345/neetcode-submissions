class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #no possible distinct index duplicaete
        if len(nums) < 1:
            return False
        
        L=0
        window = set()
        for R in range(len(nums)):
            #shift window if size reached
            if R-L > k:
                window.remove(nums[L])
                L += 1
            #check if duplicate in set
            if nums[R] in window:
                return True
            #add to window otherwise
            window.add(nums[R])

        return False 