class Solution:
    #O(2^N) as each iterat of n elemnt array can make 2 choice, take element or not
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubSets = []
        
        def genSubSets(curArr,i):
            #save copy of compelted subset
            if i >= len(nums):
               allSubSets.append(list(curArr)) 
               return
            
            #take current element and coninue
            curArr.append(nums[i])
            genSubSets(curArr,i+1)

            #backtrack and skip current elemetn, and continue
            curArr.pop()
            genSubSets(curArr,i+1)

 
        genSubSets([],0)
        return allSubSets