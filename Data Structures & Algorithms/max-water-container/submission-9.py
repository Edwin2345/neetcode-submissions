class Solution:
   #two pointers place at ends of container to maximze width
   #calc area, update max, and work inwards, shfiting smaller height as that limits container
   #
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        maxContainerArea = 0

        while L < R:
           maxContainerArea = max(maxContainerArea, (R-L)*min(heights[R],heights[L]))
           if heights[L] < heights[R]:
              L += 1
           else:
              R -= 1
         
        return maxContainerArea