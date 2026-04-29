class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #start at ends and work towards middle -> compute array
        maxA = 0
        L=0
        R=len(heights)-1

        while(L < R):
            #find maxArea with curr config
            area = (R-L)*min(heights[R],heights[L])
            maxA = max(maxA, area)

            #shift the smaller edge inward -> as that is what limits height
            if heights[L] == heights[R]:
               L += 1
               R -= 1 
            elif heights[L] < heights[R]:
               L += 1
            elif heights[R] < heights[L]:
               R -= 1  

        return maxA