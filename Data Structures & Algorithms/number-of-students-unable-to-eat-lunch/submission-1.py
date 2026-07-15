class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        square = 0
        circle = 0
        cur_sandwich = 0
        n = len(sandwiches)

        for student in students:
            if student == 1:
                square += 1
            else: 
                circle += 1
        
        while cur_sandwich < n:
            if sandwiches[cur_sandwich] == 1 and square != 0:
                square -= 1
            
            elif sandwiches[cur_sandwich] == 0 and circle != 0:
                circle -= 1
            
            else:
                break
            
            cur_sandwich += 1
        
        return square + circle
