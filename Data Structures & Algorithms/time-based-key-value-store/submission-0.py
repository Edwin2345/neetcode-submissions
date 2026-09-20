class TimeMap:
    #Q -> will we have strictly increasing timestamps -> yes 
       # -> i guess that also implese you wont overwrite a timestamp -> yes
    #N -> we have to handle invalid gets with ""
    def __init__(self):
        self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        #if key does not exist create it, otherwise append it to end        
        if key not in self.store:
           self.store[key] = [(timestamp, value)]
           return
        self.store[key].append( (timestamp, value) ) 
        
    def get(self, key: str, timestamp: int) -> str:
        # key not found
        if key not in self.store:
           return ""  
        # all timestamps are strictly larger
        if self.store[key][0][0] > timestamp:
           return ""

        #otherwise binary search to find timestamp_prev closest to target   
        values = self.store[key]
        L, R = 0, len(values)-1
        valueIndex = -1
        while L <= R:
            M = L + (R-L)//2
            #found a valid value <= timestamp, store it and try to find later value
            if values[M][0] <= timestamp:
               valueIndex = M 
               L = M + 1
            #timestmap to large, search lower vlaues
            else:
               R = M - 1
        return values[valueIndex][1]
     

