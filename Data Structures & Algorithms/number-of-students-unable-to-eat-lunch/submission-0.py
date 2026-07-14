class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stud_head = 0
        sand_head = 0
        not_eaten = 0
        length = len(students)

        while stud_head != len(students) and not_eaten != length:
            if students[stud_head] == sandwiches[sand_head]:
                sand_head += 1
                not_eaten = 0
            
            else:
                if not_eaten == 0:
                    length = len(students) - stud_head
                students.append(students[stud_head])
                not_eaten += 1
            
            stud_head += 1
        
        return not_eaten
