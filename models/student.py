class Student:
    def __init__(self, name, student_id, grades=None):
        self.name = name
        self.student_id = student_id
        if grades is None:
            self.grades = []
        else:
            self.grades = grades 

    def gpa(self): 
        if self.grades:
            avg = sum(int(grade) for grade in self.grades)/len(self.grades)
            return round(avg, 2)
        else: 
            return 0 
        
       
    
    gpa = property(gpa)

    def to_dict(self):
        return {
            "name": self.name,
            "grades": self.grades,
            "student_id": self.student_id
        }
    
    def add_grade(self, grade):
        if type(grade) is int:
            if 0 <= grade <- 100:
                self.grades.append(grade)
            else:
                raise ValueError 
        elif type(grade) is str:
            if grade.isnumeric() & 0 <= int(grade) <= 100: 
                self.grades.append(grade) 
            else:
                raise ValueError
        else:
            raise ValueError



    