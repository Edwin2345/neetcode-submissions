class Solution:
    #N: can return solution in any order
    #N: only lowercase letters
    #P: for each word, calc its freq in an int[26] array
    #P: turn freqArr into tuple (hash key), place into map freqArr 
    #P: turn into list of lists
    #Time COmpleity -> O(N*k) where k is lenght of largest word (during freq arr build) Space compleixty: O(n) to build map
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = {}
        for s in strs:
            #build freq arr
            freqArr = [0]*26
            for ch in s:
                freqArr[ord(ch)-ord("a")] += 1
            
            #add to map
            key = tuple(freqArr)
            if key not in freqMap:
               freqMap[key] = [s]
            else:
               freqMap[key].append(s)
        
        #turn into list of lsit
        groups = []
        for g in freqMap.values():
            groups.append(g)
        return groups
       