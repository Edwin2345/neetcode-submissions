class Solution:
    # positive nums
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        allSums = []

        # sort list to get duplicates side by side
        candidates.sort()

        def dfs(i, curSum, curList):
            if curSum == target:
                allSums.append(list(curList))
                return
            if curSum > target:
                return
            if i == len(candidates):
                return

            # take current number and go to next index (one use allowed)
            curSum += candidates[i]
            curList.append(candidates[i])
            dfs(i + 1, curSum, curList)

            # backtrack and go to next unique index
            curSum -= candidates[i]
            curList.pop()
            j = i + 1
            while j < len(candidates):
                if candidates[j] != candidates[i]:
                    break
                j += 1

            dfs(j, curSum, curList)

        dfs(0, 0, [])
        return allSums
