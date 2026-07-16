class Solution:
    #Rotatted sortd makes two sored halfs, LST and RST
    #minimu value occurs at begining of RST
    def findMin(self, nums: List[int]) -> int:
        minVal = float("inf")
        L = 0
        R = len(nums) - 1
        while L <= R:
            mid = L + (R-L)//2
            #we are in RSH, take min and try to go more lef tot beiging of RSH
            if nums[mid] <= nums[R]:
               minVal = min(minVal, nums[mid])
               R = mid - 1
            #we are in LSH, try moving right               
            else:
               L = mid + 1         

        return minVal
        