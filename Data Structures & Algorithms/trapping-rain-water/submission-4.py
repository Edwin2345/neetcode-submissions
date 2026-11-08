class Solution:
    # approach: find amount trapped at eahc index (width of 1) and sum
    # formula: area of water trap =  (min(maxLeftHeight, maxRightHeight) - height[i])*1 (for width)
    # Optimization: store the max height from left and right side using prefix/suffix array
    # compute once and use throghout
    # O(N) time to make prefix/suffix array and O(N) space to store both the arrays
    def trap(self, height: List[int]) -> int:
        totalWater = 0

        # compute the left and right max heights for every index
        leftMaxHeight, rightMaxHeight = [0] * len(height), [0] * len(height)
        for i in range(1, len(height)):
            leftMaxHeight[i] = max(leftMaxHeight[i-1], height[i - 1])
        for i in range(len(height) - 2, -1, -1):
            rightMaxHeight[i] = max(rightMaxHeight[i+1], height[i + 1])

        #for each index (grid of width 1) find how much water it hold
        for i in range(len(height)):
            heightDrop = min(leftMaxHeight[i], rightMaxHeight[i]) - height[i]
            if heightDrop > 0:
               totalWater += heightDrop*1 

        return totalWater
