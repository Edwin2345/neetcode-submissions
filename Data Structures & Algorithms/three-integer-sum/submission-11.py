class Solution:
    #betetr: sort nums, then fix one numebr and two poitner search the remaing widnow
    #skip duplicates throguhout
    # TC O(N^2), SC: O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        #sort so that two pointer trick works O(nlogn)
        nums.sort()

        # this is like O(n^2)?
        for i in range(len(nums)):
            #skip duplicate nums
            if i > 0 and nums[i] == nums[i-1]:
               continue

            #search for 2 other nums hat total to zero
            L,R = i+1, len(nums) - 1
            while L < R:
                sm = nums[i] + nums[L] + nums[R]

                #foudn valid tripplet, shift both inward skipping duplicates
                if sm == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1  
                    while L < R and nums[R] == nums[R+1]:
                        R -= 1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
                #sum too large, shift window right (skipping duplicates) to smaller num
                elif sm > 0:
                    R -= 1
                    while L < R and nums[R] == nums[R+1]:
                        R -= 1
                #sum too small, shift window left (skipping duplicates) to larger num
                else:
                    L += 1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
            
        return res               
        