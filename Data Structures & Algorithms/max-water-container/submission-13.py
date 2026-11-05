class Solution:
    #linear solution, start at both ends to maximize widht and compute area
    #onyl compute area of rectangles that has chance of increasing the current height
    #meaning you shift the smller side inwards as it is the one the limits height, givign you larger area
    #O(N) time as linear scna, O(1)
    def maxArea(self, heights: List[int]) -> int:
        maxRectArea = 0 
        L,R = 0, len(heights) - 1

        while L < R:
           #calc current area and update max
           rectArea = (R-L)*min(heights[L], heights[R])
           maxRectArea = max(maxRectArea, rectArea)

           #shift smalelr side inwards, if both small shift both inward
           if heights[L] == heights[R]:
              L += 1
              R -= 1
           elif heights[L] < heights[R]:
              L += 1
           else:
              R -= 1


        return maxRectArea