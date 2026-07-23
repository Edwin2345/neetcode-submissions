class Solution:
    #o(nlogn) + o(n^2) = o(n^2) solution
    #sort, fix one end and use two poitners on the remaining
    #need to skip duplciates at all 3 points
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        validTriplets = []

        #sort
        nums.sort()

        for i in range(len(nums)):
            #skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
               continue 
            
            #use two pointers to fidn ther two value
            L = i+1
            R = len(nums)-1
            while L < R:
                sm = nums[i] + nums[L] + nums[R]
                #found valid pair
                if sm == 0:
                   #add to final answer
                   validTriplets.append( [nums[i], nums[L], nums[R]] ) 

                   #shift inwards and skip duplicates
                   L += 1
                   R -= 1
                   while L <= len(nums)-1 and nums[L] == nums[L-1]:
                        L += 1
                   while R >= 0 and nums[R] == nums[R+1]:
                        R -= 1  
                #too large, shift left
                elif sm > 0:
                   R -= 1
                #too small, shift right   
                else: 
                   L += 1          
                
        return validTriplets
        