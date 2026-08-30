class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #make adj list
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for course, preCourse in prerequisites:
            adj[preCourse].append(course)
        
        #go through every course and post order dfs to build top order
        topOrder = []
        visitedSet, pathSet = set(), set()
        for course in adj.keys():
            if not self.dfs(course, adj, pathSet, visitedSet, topOrder):
               return []

        #reverse to get correct top order
        topOrder.reverse()
        return topOrder

    def dfs(self, course, adj, pathSet, visitedSet, topOrder):
        #edge case: cyclical pre-req
        if course in pathSet:
           return False
        #base case: already explored all child courses 
        if course in visitedSet:
           return True

        #add course to path and explore child courses
        pathSet.add(course)
        for childCourse in adj[course]:
            if not self.dfs(childCourse, adj, pathSet, visitedSet, topOrder):
               return False

        #add course to top order, mark as visited, remove from path
        topOrder.append(course)
        visitedSet.add(course)
        pathSet.remove(course)
        return True

