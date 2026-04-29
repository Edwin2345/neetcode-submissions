class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force
        maxArea = 0
        for L in range(len(heights)):
            for R in range(L+1, len(heights)):
                currArea = (R-L)*min(heights[L],heights[R])
                maxArea = max(currArea,maxArea)
        return maxArea