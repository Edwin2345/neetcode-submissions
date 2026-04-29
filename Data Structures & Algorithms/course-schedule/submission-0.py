class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #build adjacency list of prereq (courses numebred from 0 to numCourse-1)
        adjList = [[] for i in range(numCourses)]
        for course,prereq in prerequisites:
            adjList[course].append(prereq)

        #dfs to find if there is valid path to take a given  
        visiting = set()
        def dfs(course, path=[]):
            #circular dependacy -> no path
            if course in visiting:
               return False
            #no prereqs blocking _. found path to take course
            if adjList[course] == []:
               return True
            
            #add course to visiting
            visiting.add(course)
            path.append(course)

            #check prerequesits are also possible to complete
            for prereq in adjList[course]:
                if not dfs(prereq):
                   return False

            #clear prereqs once verified ath
            print(path)
            visiting.remove(course) 
            adjList[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
            
