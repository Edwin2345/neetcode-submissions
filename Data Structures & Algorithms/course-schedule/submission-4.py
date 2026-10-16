class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create adj list
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for course, pre in prerequisites:
            adj[pre].append(course)
        
        #post order dfs for topo sort
        topOrder = []
        visited = set()
        path = set()

        def dfs(course):
            #cyclical prereq
            if course in path:
               return False 
            #already explored this courses children
            if course in visited:
               return True
            
            #add to path add dfs its downstrem courses (children)
            path.add(course)
            for childCourse in adj[course]:
                if not dfs(childCourse):
                   return False 

            #add to top order, mark as visited and remove from path
            topOrder.append(course)
            visited.add(course)
            path.remove(course)
            return True


        #top sort: do post order dfs on all course:
        for course in range(numCourses):
            if not dfs(course):
               return False

        topOrder.reverse()
        print(topOrder)
        return True 
