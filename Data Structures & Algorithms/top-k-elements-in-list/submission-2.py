class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ 
        1. count freq of elements with map
        2. create an array of size len(nums) -> each index i stores a list of nums with freq i
        3. traverse backwards until k elements have been found
        """
        freqCnt = {}
        cntArr = [[] for i in range(len(nums)+1)]
        topK = []

        #count freq of elements in num
        for n in nums:
            if n in freqCnt:
                freqCnt[n] += 1
            else:
                freqCnt[n] = 1 
        
        #for all frequencies, populate cntArr
        for n,freq in freqCnt.items():
            cntArr[freq].append(n)
        
        #traverse from higher freq to lower, adding elements to form topK list
        for freq in range(len(cntArr)-1,-1,-1):
            for n in cntArr[freq]:
                topK.append(n)
                #stop once k elements have been found
                if len(topK) == k:
                   return topK