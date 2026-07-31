class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #sort to get duplciates side by side
        nums.sort()
        allSubsets = []

        def genAllSubsets(curArr, i):
            if i >= len(nums):
               allSubsets.append(list(curArr))
               return
            
            #take the current elememt, and go to next
            curArr.append(nums[i])
            genAllSubsets(curArr, i+1)
            
            #backtrack -> pop current elemnt, and skip all duplcaites
            curArr.pop()
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                  i += 1
            genAllSubsets(curArr, i)

        genAllSubsets([],0)
        return allSubsets
