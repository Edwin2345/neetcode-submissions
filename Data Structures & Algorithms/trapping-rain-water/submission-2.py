class Solution:
    #O(n), O(1) -> L and R poitners at both ends
    # compute leftMax and rightMax up front
    #: use that info to compute area of each 1 width bucket workign inwards
    def trap(self, height: List[int]) -> int:
        totalRainArea = 0
        L,R = 0, len(height)-1
        leftMaxHeight, rightMaxHeight = height[0], height[-1]

        while L < R:
            #determine which is the limitign side
            if leftMaxHeight < rightMaxHeight:
               #compute how much water trapped at current index
               trappedWater = leftMaxHeight - height[L]
               totalRainArea += max(trappedWater, 0)

               #shift and update left max height
               L += 1
               leftMaxHeight = max(leftMaxHeight, height[L])
            else: 
               #compute how much water trapped at current index
               trappedWater = rightMaxHeight - height[R]
               totalRainArea += max(trappedWater, 0)

               #shift and update right max height
               R -= 1
               rightMaxHeight = max(rightMaxHeight, height[R]) 

        return totalRainArea
        