class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubsets = []
        
        def findSubsets(curSubset, i):
            #reached end of decision tree, store subset
            if i == len(nums):
               allSubsets.append(list(curSubset))
               return

            #take current element and proceed makign subset
            curSubset.append( nums[i] )
            findSubsets(curSubset, i+1)

            #skip this current element and proceed
            curSubset.pop()
            findSubsets(curSubset, i+1)

        findSubsets([],0)
        return allSubsets