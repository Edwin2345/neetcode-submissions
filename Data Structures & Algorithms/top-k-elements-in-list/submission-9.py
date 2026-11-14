class Solution:
    #bucket sort based on freq, use a fixed array of 0 to len(nums)
    #TC: O(N),  SC O(N)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count freq of nums 
        #O(N) TC, O(N) SC
        numFreq = defaultdict(int)
        for n in nums:
            numFreq[n] += 1
        
        #add nums to "buckets" --> index is freq, list of lists
        #O(N) TC, O(N) SC
        buckets = [[] for _ in range(len(nums) + 1)]
        for num,freq in numFreq.items():
            buckets[freq].append(num)
        
        #get to k most frequent --> O(K) TC, O(1) extra sapace
        res = []
        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                res.append(num)
                #found k elements
                if len(res) == k:
                   return res 

        #found less than k elements
        return res
        