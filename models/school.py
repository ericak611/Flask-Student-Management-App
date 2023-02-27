import json 
from models.student import Student
import operator 

class School:
    def __init__(self, filename): 
        self.filename = filename
        self._student = {}
        self.name = ""
        self.load_from_json()  

    def load_from_json(self):
        with open(self.filename, "r") as fp:
            self.file = json.load(fp) 
            self.name = self.file["name"]
            self.students = self.file["students"]
             
        
        for i in self.students:
            name = i["name"] 
            student_id = i["student_id"] 
            grades = i["grades"] 
            self._student[student_id] = (Student(name, student_id, grades)) 
        
        
        
    def get_students(self, sorted_by):
        if sorted_by == "name":
            return sorted(self._student.values(), key=operator.attrgetter("name"), reverse = False)
        elif sorted_by == "gpa": 
            return sorted(self._student.values(), key=operator.attrgetter("gpa"), reverse = True)

    def get_student(self, student_id): 
        if student_id in self._student:
            return self._student[student_id] 
        else:
            return None
        

    def to_dict(self):
        student_list = []
        for i in self._student.values():
            info = Student.to_dict(i)
            student_list.append(info)
            
        return {
            "name": self.name,
            "students": student_list 
        }
    
    def save(self):
        with open(self.filename, "w") as wf:
            json.dump(School.to_dict(self), wf)
    
    def __len__(self):
        return len(self.file)
    
    def add_student(self, name, student_id):
        if not name or not student_id:
            raise ValueError 
        elif student_id in self._student:
            return False 
        else:
            self._student[student_id] = (Student(name, student_id)) 
            return True   
        # if not name or not student_id:
        #     raise ValueError
        # else:
        #     for each_student in self._students:
        #         if each_student == student_id:
        #             raise TypeError
        #         else:
        #             continue

        #     student_instance = Student(name, student_id, grades=None)
        #     self._students[student_id]=student_instance

            
        #     return True 

        
