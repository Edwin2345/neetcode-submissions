class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #we need to skip over duplicates in one branch, and take the duplicatin in order
        #sort, so we get duplciates side by side O(nlogn)
        nums.sort()
        allSubsets = []
        curSubset = []

        def findSubsets(index):
            #finsiehd making subset
            if index == len(nums):
               allSubsets.append(list(curSubset))
               return

            #take current element
            curSubset.append( nums[index] )
            findSubsets(index + 1)

            #backtrakc -> don't take element, and skip over any duplicates
            curSubset.pop()
            curVal = nums[index]
            while index < len(nums) and nums[index] == curVal:
                index += 1
            findSubsets(index)

        findSubsets(0)
        return allSubsets