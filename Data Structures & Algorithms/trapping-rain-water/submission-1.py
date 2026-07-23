class Solution:
    #O(n) time, O(n) space -. same min(maxLeftHeights, maxRightHeights) - height[pos] but use prefix array
    def trap(self, height: List[int]) -> int:
        #build prefix and suffix arreas fro max leght height and right height
        maxLeftHeights, maxRightHeights = [0]*len(height), [0]*len(height)        
        for i in range(1, len(height)):
            maxLeftHeights[i] = max(maxLeftHeights[i-1], height[i-1])
        for i in range(len(height)-2, -1, -1):
            maxRightHeights[i] = max(maxRightHeights[i+1], height[i+1])
        
        #compute total rain area by finding how much water each positon holds
        totalRainArea = 0
        for i in range(len(height)):
            trappedWater = (min(maxLeftHeights[i], maxRightHeights[i]) - height[i])*1
            if trappedWater > 0:
               totalRainArea += trappedWater

        return totalRainArea 
        