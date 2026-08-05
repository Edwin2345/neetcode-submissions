class Solution:
    #brute force: O(n^2) time, iterate throguh array, then search for a hotter day
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        daysTillHotter = [0] * len(temperatures)

        for i in range(len(temperatures)):
            dayCount = 0 
            for j in range(i+1,len(temperatures)):
                dayCount += 1
                #found hotter day
                if temperatures[j] > temperatures[i]:
                   daysTillHotter[i] = dayCount
                   break 
        
        return daysTillHotter
                   
        