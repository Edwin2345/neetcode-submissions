class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #build adj list: course: [down strema courses]
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for course, pre in prerequisites:
            adj[pre].append(course)
        
        #post order dfs function
        topOrder, visited, path = [], set(), set()
        def dfs(course):
            #cyclic dependacies -> no possible schedule
            if course in path:
               return False 
            #already found course and its child courses
            if course in visited:
               return True

            #add current course to path and run dfs on down stema child courses
            path.add(course)
            for childCourse in adj[course]:
                if not dfs(childCourse):
                   return False   
            
            #add course to topologic order, mark as visited and remove from path
            topOrder.append( course )
            visited.add( course )
            path.remove( course )
            return True
        
        #run post order dfs on every course to build schedule
        for course in range(numCourses):
            if not dfs(course):
               return []

        #reverse to get correct top order
        topOrder.reverse()
        return topOrder
