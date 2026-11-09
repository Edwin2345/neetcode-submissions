class TimeMap:
    #set is called with stricly increasing time stamps
    #get shoudl return the timestamp that is <= to it
    #use a dict --> key: [ valueTuples]
    class StoredValue:
        def __init__(self, value, timestamp):
            self.value = value
            self.timestamp = timestamp

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        newStoredValue = self.StoredValue(value, timestamp)

        if key not in self.store:
           self.store[key] = [newStoredValue]
           return

        self.store[key].append(newStoredValue)
        
    def get(self, key: str, timestamp: int) -> str:
        #no key found
        if key not in self.store:
           return ""

        #bianry search for larget rpeceding timestample
        valueList = self.store[key]
        L,R = 0, len(valueList) - 1
        foundValue = None
        while L <= R: 
            #calc middle index
            M = L + (R - L)//2

            #found valid stored value, save and try to search higher
            if valueList[M].timestamp <= timestamp:
               if foundValue is None or foundValue.timestamp < valueList[M].timestamp:
                  foundValue = valueList[M]
               L = M + 1
            #timestamp too large, search lower half
            else:
               R = M - 1
        
        return foundValue.value if foundValue else ""
                
        
