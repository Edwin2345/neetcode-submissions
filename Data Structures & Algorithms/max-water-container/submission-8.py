class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights)-1
        largestArea = 0
        
        while L < R:
              #calc current area and update max
              curArea = (R-L)*min(heights[L], heights[R])
              largestArea = max(largestArea, curArea)

              #shift the smaller edge
              if heights[L] < heights[R]:
                 L += 1
              else:
                 R -= 1 

        return largestArea