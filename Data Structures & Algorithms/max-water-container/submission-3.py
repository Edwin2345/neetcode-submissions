class Solution:
    def calcArea(self, heights, L, R):
        return (R-L)*min(heights[L],heights[R])

    def maxArea(self, heights: List[int]) -> int:
        #sliding window -> start at ends because want to maximize area STUPID
        maxArea = 0
        L=0
        R=len(heights)-1
        while(L < R):
            maxArea = max(maxArea, self.calcArea(heights,L,R))
            #update the limiting (smaller height) pointer, as already stored max possible area (both ends)            
            #if both are equal, move one inward as already stored max area for that height
            if heights[L] < heights[R]:
                L += 1
            elif heights[R] < heights[L] or heights[L] == heights[R]:
                R -= 1

        return maxArea