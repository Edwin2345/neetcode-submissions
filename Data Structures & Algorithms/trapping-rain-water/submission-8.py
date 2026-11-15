class Solution:
    # sum up the amoutn fo rain water help by each slice of width 1 (each index)
    # amont held by index = min((min(leftMaxHeight, rightMaxHeight) - height[i]) * 1, 0)
    # edges hold nothign so start 1 inwards: L=1, R=len(height)-2,
    # leftMaxHeight, rightMaxHeight = heights[0], heights[-1]
    # find the smaller max height, calualte water held adjacent to that edge, and update max
    def trap(self, height: List[int]) -> int:
        totalWater = 0
        leftMaxHeight, rightMaxHeight = height[0], height[-1]
        L, R = 0, len(height) - 1

        while L < R:
            # find the smaller max height, find water held adjacent to that edge, update max
            if leftMaxHeight < rightMaxHeight:
                totalWater += max((leftMaxHeight - height[L + 1]) * 1, 0)
                leftMaxHeight = max(leftMaxHeight, height[L + 1])
                L += 1
            else:
                totalWater += max((rightMaxHeight - height[R - 1]) * 1, 0)
                rightMaxHeight = max(rightMaxHeight, height[R - 1])
                R -= 1

        return totalWater
