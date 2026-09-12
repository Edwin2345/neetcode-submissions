class Solution:
    #idea: simulate this usign max_heap and a cooldown min_heap, greedly scheule msot freqnt task
    #max_heap stores msot freqtuent tasks, coolDown is used to store tasks by shortest time remainign until can be reschuled
    #time complexity: O(N) where n is numebr of task -> need to build freq map and hepa operations are o(1) as only 26 states
    #space complexity: O(N) for freq map and the 2 heaps
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #build max_heap based on freq of state
        freqMap = defaultdict(int)
        for t in tasks:
            freqMap[t] += 1
        max_heap = [ (-freq, state) for state,freq in freqMap.items()]
        heapq.heapify(max_heap)

        #simulate
        time, coolDown = 0, []
        #schedule = []
        while len(max_heap) > 0 or len(coolDown) > 0:
            #move tasks that are done cooldown into max_heap
            while len(coolDown) > 0 and coolDown[0][0] <= time:
                _, freq, state = heapq.heappop(coolDown)
                heapq.heappush(max_heap, (-freq, state))
            
            #schedule the most frequent task at thsi current time, and place into cooldown if still need to schedule
            if len(max_heap) > 0:
               negFreq, state = heapq.heappop(max_heap)
               # schedule.append( state )
               freq = negFreq * -1
               
               freq -= 1
               if freq > 0:
                  heapq.heappush( coolDown, (time + n + 1, freq, state) )
            #no task to schedule at this point of time
            #else:
            #   schedule.append( "idle" )

            #increment time
            time += 1

        # print(schedule)
        return time 

       

        
            