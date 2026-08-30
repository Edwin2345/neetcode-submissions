class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #turn into adj list {course: [child courses]}
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for course, pre in prerequisites:
            adj[pre].append(course)
        

        #run dfs on every graph course -> use path set to tell if cycle
        visitedSet = set()        
        pathSet = set()
        for course in adj.keys():
            if not self.dfs(course, adj, pathSet, visitedSet):
               return False 

        return True
    
    def dfs(self, course, adj, pathSet, visitedSet):
        #foudn cycle as child course is a prereq to some parent
        if course in pathSet:
           return False 
        #already fully explored children of this couse
        if course in visitedSet:
           return True 
        
        #mark current course as on path -> then recurse to engihbors
        pathSet.add(course)
        for nei in adj[course]:
            if not self.dfs(nei, adj, pathSet, visitedSet):
               return False

        #mark this node as visited (no ciruclar preqs detected) 
        #and remove from path 
        visitedSet.add(course)
        pathSet.remove(course)
        return True
        
