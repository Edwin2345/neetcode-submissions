class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #memoizing turns TC: O(W^(S/M)) into O(S*W). (*L if you acocutn for substrign comb)
        #space still O(S)
        cache = {}
        def canBreakWord(i):
            # finished breakign word
            if i == len(s):
                return True
            #already computed if tis possilbe or not
            if i in cache:
               return cache[i] 

            # otherwise, try all possible words to break starting
            # from here
            for word in wordDict:
                wordLen = len(word)
                if i + wordLen > len(s):
                    continue
                if s[i : i + wordLen] == word and canBreakWord(i + wordLen):
                    cache[i] = True
                    return cache[i]

            # couldn't break
            cache[i] = False
            return cache[i]

        return canBreakWord(0)
