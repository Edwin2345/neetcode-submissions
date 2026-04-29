class Solution:
    def originDist(self,p):
        return ((p[0])**2 + (p[1])**2)**0.5 

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #create a list of tuples for comparison
        distList = [(self.originDist(p), p[0], p[1]) for p in points]

        #heapify that list -> uses distance to create min heap
        heapq.heapify(distList)

        #get top k elements in heap (closest)
        kCloseList = []
        for i in range(k):
            el = heapq.heappop(distList)
            kCloseList.append([el[1], el[2]])
        
        return kCloseList
        