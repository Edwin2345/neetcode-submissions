class Solution:
    # approach: find amount trapped at eahc index (width of 1) and sum
    # formula: area of water trap =  (min(maxLeftHeight, maxRightHeight) - height[i])*1 (for width)
    # Optimization: we can calcualte leftMax and right max once by working from ends inwards
    # O(N) time as 1 linear scan, O(1) space as jsut use variables
    def trap(self, height: List[int]) -> int:
        totalWater = 0
        leftMaxHeight, rightMaxHeight = height[0], height[-1]
        L,R = 0, len(height) -1

        while L < R:
            #left height is limiting
            if leftMaxHeight < rightMaxHeight:
               # shift inwards to compute water trapped by this boudnry, the updat max boudnry height
               L += 1
               totalWater += max( (leftMaxHeight - height[L])*1, 0)
               leftMaxHeight = max(height[L], leftMaxHeight)
            #right height is limiting
            else:
               # shift inwards to compute water trapped by this boudnry, the updat max boudnry height
               R -= 1
               totalWater +=  max( (rightMaxHeight - height[R])*1, 0)
               rightMaxHeight = max(height[R], rightMaxHeight)

        return totalWater
