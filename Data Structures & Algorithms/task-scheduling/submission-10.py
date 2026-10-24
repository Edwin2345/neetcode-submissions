class Solution:
    # cycle counter variable
    # maxFreq heap (freq, taks), coolDown queue (cycleWhenRescheduable, freq, task)
    # most freq max heap: "A" (3,A) --> (2,A) and add to min cooldown heap (3, 2, A)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #add tasks to max heap by freq
        freqMap = defaultdict(int)
        for t in tasks:
            freqMap[t] += 1

        maxFreqHeap = []
        for t,cnt in freqMap.items():
            heapq.heappush(maxFreqHeap, (cnt * -1, t))
        
        #simulate
        cycle = 0
        coolDownQueue = deque()

        while len(maxFreqHeap) > 0 or len(coolDownQueue) > 0:
            # add all tasks back to freq heap that have finished cooling down
            while len(coolDownQueue) > 0 and coolDownQueue[0][0] <= cycle:
                cycleWhenReshedulable, negFreq, task = coolDownQueue.popleft()
                heapq.heappush( maxFreqHeap,  (negFreq, task))
            
            # take the modt frequent task and schedule it at current cylece
            # then add back to coolDownQueue if still tasks of that type left
            if len(maxFreqHeap) > 0:
               negFreq, task = heapq.heappop( maxFreqHeap )
               negFreq += 1

               if negFreq < 0:
                  coolDownQueue.append( (cycle + n + 1, negFreq, task) )

            #go to next cycle
            cycle += 1

        return cycle