class Solution:
    #idea: simulate this usign max_heap and queue, greedly scheule msot freqnt task
    #max_heap stores msot freqtuent states, queue is used to order tasks based on cooldown
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #build max_heap based on freq of state
        freqMap = defaultdict(int)
        for t in tasks:
            freqMap[t] += 1
        max_heap = [ (-freq, state) for state,freq in freqMap.items()]
        heapq.heapify(max_heap)

        #simulate
        time, coolDownQ = 0, deque()
        # simulation = []
        while len(max_heap) > 0 or len(coolDownQ) > 0:
            #put tasks back into max_heap that are done cooldown
            while coolDownQ and coolDownQ[0][2] <= time:
                freq, state, _ = coolDownQ.popleft()
                heapq.heappush( max_heap, (-freq,state))
            
            #check max-heap to scheudle most frequent task at this time
            #add to cooldown once dowe
            if len(max_heap) > 0:
               negFreq, state = heapq.heappop(max_heap)
              # simulation.append( state )
               freq = negFreq*-1
               freq -= 1

               if freq > 0:
                  coolDownQ.append( (freq, state, time + n + 1) )
            #nothing in heap: nothing to do at this time
            #else:
            #   simulation.append("idle") 

            #go to next time point
            time += 1
      
        #print(simulation)
        return time

        
            