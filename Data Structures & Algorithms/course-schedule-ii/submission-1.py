class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #make adj list
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for course, pre in prerequisites:
            adj[pre].append(course)
        
        #post order dfs for top sort
        topOrder, visited, path = [], set(), set()
        def dfs(course):
            #pre-req conflict
            if course in path:
               return False 
            #already vistied coruse and its decendances
            if course in visited:
               return True

            #add course to path and dfs to children
            path.add(course)
            for childCourse in adj[course]:
                if not dfs(childCourse):
                   return False

            #add to top order, makr visted and remove form path
            topOrder.append(course)
            visited.add(course)
            path.remove(course)  
            return True
        
        #top sort: post order dfs every course
        for course in range(numCourses):
            if not dfs(course):
               return [] 

        topOrder.reverse()
        return topOrder