class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #build adj list --> course: descendants
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for course, prereq in prerequisites:
            adj[prereq].append(course)

        #post order dfs function
        topOrder, visited, path = [], set(), set()
        def dfs(course):
            #circular dep
            if course in path:
               return False 
            #already computed path from course to all its decents
            if course in visited:
               return True 
            
            #add course to path, and recurse to its children
            path.add(course)
            for descendant in adj[course]:
                if not dfs(descendant):
                   return False 
            
            #add course to top order, mark as visited, remove from path
            topOrder.append(course)
            visited.add(course)
            path.remove(course)
            return True
        
        #top sort: run post order dfs starting from all courses
        for course in range(numCourses):
            if not dfs(course):
               return []
        
        #reverse to get top order
        topOrder.reverse()
        return topOrder
