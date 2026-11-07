class TimeMap:
    # set is called with stricly increasing time stamps
    # get shoudl return the timestamp that is <= to it
    # use a dict --> key: [ valueTuples]
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
        # no key found
        if key not in self.store:
            return ""

        # binary search to find the largest preceeding or equal timestamp
        # we can do that as timestamps as sorted (strictly ineasing)
        valueList = self.store[key]
        L, R = 0, len(valueList) - 1
        foundValue = ""
        while L <= R:
            M = L + (R - L) // 2
            # found valid timestamp, save and try to move to a lrger timstamp
            if valueList[M].timestamp <= timestamp:
               foundValue = valueList[M].value 
               L = M + 1
            # timestamp to large, search lower half
            else:
                R = M - 1

        # last valid timestamp is where the two pointers converge
        return foundValue
