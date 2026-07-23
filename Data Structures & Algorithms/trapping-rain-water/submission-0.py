class Solution:
    #brute force: consider each poisiton as bucket of width 1
    #The amount of water we can store at that posiuotn = min(maxLeftHeight, maxRightHeight) - height[pos]
    #the leftMaxHeight and rightMaxHeight are found by searching 0,i-1 and i-1,len-1 respectively
    #O(N^2) time and O(1) space
    def trap(self, height: List[int]) -> int:
        totalRainArea = 0
        
        for i in range(len(height)):
            #compute max left and right heights at this poitionb
            maxLeftHeight, maxRightHeight = 0, 0 
            for j in range(i):
                maxLeftHeight = max(maxLeftHeight, height[j])
            for k in range(i+1,len(height)):
                maxRightHeight = max(maxRightHeight, height[k])

            #add on area of water we can hold at that position
            trappedWater = (min(maxLeftHeight, maxRightHeight) - height[i]) * 1
            if trappedWater > 0:
               totalRainArea += trappedWater

        return totalRainArea
        