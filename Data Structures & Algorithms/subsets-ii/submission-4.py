class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # sort to get duplicates side by
        allSubsets = []
        nums.sort()

        def dfs(i, curSubset):
            # compelted subset
            if i == len(nums):
                allSubsets.append(list(curSubset))
                return

            # decision to take num current index
            curSubset.append(nums[i])
            dfs(i + 1, curSubset)

            # bactrack, remove current num and skip to next decision
            # which is the next unique number
            curSubset.pop()
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            dfs(j, curSubset)

        dfs(0, [])
        return allSubsets
