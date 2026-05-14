class Solution:
    def generateFreqStr(self,s):
        freqArr = [0]*26
        for w in s:
            freqArr[ord(w)-ord("a")] += 1
        return ",".join([str(f) for f in freqArr])

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #generate map that contains str of freq count : [strings]
        freqMap = {}
        for s in strs:
            freqStr = self.generateFreqStr(s)
            if freqStr in freqMap:
               freqMap[freqStr].append(s)
            else:
               freqMap[freqStr] = [s]  

        #iterate through values of that map to make list of list
        res = []
        for v in freqMap.values():
            res.append(v)
        
        return res

        