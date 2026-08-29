class Solution:
    #sort by positon decreasing
    #measure the time for furtest to reach target
    #if a car at a position prior reaches earlier -> same car fleet
    #else, increment car fleet number as reahc at seperat times
    #continue by working down, tkaing max of the times
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #create tuples and sort by position decending
        carTuples = []
        for i in range(len(speed)):
            carTuples.append( (position[i], speed[i]) )
        carTuples.sort(key=lambda x:(x[0], x[1]), reverse=True)
        
        #starting from furtest positon, calc time till target,
        numCarFleets = 0
        timeOfCarAhead = -1
        for pos,speed in carTuples:
            timeTillArrival = (target-pos)/speed
            #car at further back position arrives after the one in front -> new fleet
            if timeTillArrival > timeOfCarAhead:
               numCarFleets += 1
            timeOfCarAhead = max(timeOfCarAhead, timeTillArrival)
        
        return numCarFleets