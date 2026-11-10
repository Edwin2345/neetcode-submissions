class Solution:
    #lowercase letters only
    #idea -> use and array of 26 ints to coutn letter freq
    #convert that array into a string to be the key for map
    #map: freqKey: [strings]

    # O(N*M) TC as call O(M) createFReqKey on N string (of max lenght M)
    # O(N*M) SC for the map and freq array
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create freq tuple of the 26 possible character 
        #TC: O(M), SC: O(1) extra space
        def createFreqKey(s):
            freqArr = [0]*26
            for letter in s:
                freqArr[ord(letter)-ord('a')] += 1

            return tuple(freqArr)
        
        #place each string into map based on freq tuple
        #O(N*M) TC, SC O(N*M) extra space for map
        anagramMap = defaultdict(list)
        for s in strs:
            freqKey = createFreqKey(s)
            anagramMap[freqKey].append(s)
        
        #cover map into 2d list
        #O(N) TC, SC O(1) extra space
        res = []
        for anagramGroup in anagramMap.values():
            res.append(anagramGroup)
        
        return res
        