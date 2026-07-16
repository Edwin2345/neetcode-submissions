class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        threeSumVals = []
        nums.sort()

        for fI,num in enumerate(nums):
            #if duplicate skip over
            if fI > 0 and nums[fI] == nums[fI-1]:
               continue

            #search for the other two nums usign two pointers
            L = fI + 1
            R = len(nums) - 1
            while L < R:
                #find 3 sum
                threeSum = nums[fI] + nums[L] + nums[R]

                #found valid threeSum
                if threeSum == 0:
                   #add triple to output array
                   threeSumVals.append([nums[fI], nums[L], nums[R]])  
                   #move poitners inwards to check next pair
                   L += 1
                   R -= 1
                   #skip duplicates on both side
                   while L < R and nums[R] == nums[R+1]:
                        R -= 1
                   while L < R and nums[L] == nums[L-1]:
                        L += 1
                #too large, move to left
                elif threeSum > 0:
                    R -= 1
                #too small, move to right
                else:
                    L += 1

        return threeSumVals