class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brute force -> o(n^2) space, o(n) mem -> for answer list
        res = []
        for i in range(len(temperatures)):
            foundHotter = False
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    res.append(j-i)
                    foundHotter = True
                    break
            if not foundHotter:
                res.append(0)
        return res