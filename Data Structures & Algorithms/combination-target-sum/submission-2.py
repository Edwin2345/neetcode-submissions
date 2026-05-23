class Solution:
    #question: assume positive only
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []
        curComb = []

        def findCombSum(i, curSum):    
            #base case, out of bounds, or blew past sume
            if i >= len(nums) or curSum > target:
               return
            #foudnd a valid path sum
            if curSum == target:
               combos.append( list(curComb) )
               return 
            
            #take current element
            curSum += nums[i]
            curComb.append(nums[i])

            #choice 1: continue at same index
            findCombSum(i, curSum)

            #backtrack
            curSum -= nums[i]
            curComb.pop()

            #choice 2; chse a differnt value for this spot
            findCombSum(i+1, curSum)

        
        findCombSum(0, 0)
        return combos
