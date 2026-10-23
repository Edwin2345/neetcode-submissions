class Solution:
    #at each index choose to take an element or not take it
    #copy lsit in o(n) time
    # tiem O(n*2^n), extra space -. O(N) for call stack
    #dont worry abotu dulkicat sets as all is unique
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubSets = []

        def dfs(index, curSet):
            #finished checking all elements
            if index == len(nums):
               allSubSets.append( list(curSet) )
               return

            #choose the current num and continue
            curSet.append( nums[index] )
            dfs(index + 1, curSet)

            #backtrack and try to make set skipping the element
            curSet.pop()
            dfs(index + 1, curSet)
        
        dfs(0, [])
        return allSubSets


        