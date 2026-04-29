class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
         create a dictionary 
               -> KEY: freq cnt array as string
               -> VALUE: array of string

               return vlaues of dictionary
        '''

        anagramDict = dict()
        for word in strs:
            #build freq string of letters in word
            freqArr = [0]*26
            for l in word:
                freqArr[ord(l)-ord('a')] += 1
            freqStr = ",".join(str(x) for x in freqArr)

            #add to freqStr to dictionary
            if freqStr in anagramDict:
                anagramDict[freqStr].append(word)
            else:
                anagramDict[freqStr] = [word]

        return list(anagramDict.values())
