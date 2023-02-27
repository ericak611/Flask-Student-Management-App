from flask import Flask, render_template, request, jsonify
from models.school import School
from models.student import Student 


app = Flask(__name__)


@app.route("/")
def home():
    school = School("./models/bcit.json")
    return render_template("list.html", school=school)

@app.route("/student/<string:student_id>")
def student(student_id):
    school = School("./models/bcit.json")
    student = School.get_student(school, student_id)
    return render_template("student.html", school=school, student=student)

@app.route("/student/add", methods=["POST"])
def add_student():
    data = request.json
    
    if "student_id" not in data.keys() or "name" not in data.keys():
        return "missing data", 400 
    
    elif "student_id" in data.keys() and "name" in data.keys():
        school = School("./models/bcit.json")
        try:
            school.add_student(data["name"], data["student_id"]) 
        except ValueError:
            return 400
        except TypeError:
            return 409


        school.save()
        return render_template("list.html", school=school)

    # data = request.json
    # if "name" in data.keys() and "student_id" in data.keys():
    #     name = data["name"]
    #     student_id = data["student_id"]

    #     school_obj = School("./models/bcit.json")
    #     try:
    #         School.add_student(school_obj, name, student_id)
    #     except ValueError:
    #         return "invalid data",400
    #     except TypeError:
    #         return "student id already exists",409

            
    #     School.save(school_obj)
    #     return render_template("list.html", school=school_obj)
    # else:
    #     return "only name provided",400
    
    # return "working"

# @app.route("/student/<str:student_id>/grades/add", methods=["POST"])
# def add_grade(student_id): 
#     data = request.json 
#     grade = data["grade"]
#     school = School("./models/bcit.json")
#     student = School.get_student(student_id)
 
#     try:
#         School.get_student(student_id)
#     except:
#         return 404
    
#     try:
#         student.add_grade(grade) 
#     except ValueError:
#         return 400
    
#     school.save()
#     return render_template("student.html", student=student), 200
        

    # if student_id not in School.get_student.keys():
    #     return 404 
    
    # elif "grade" not in data.keys():
    #     return 400

    # if data["grade"].isnumeric() & 0 <= int(data["grade"]) <= 100: 
    #     student.add_grade(data["grade"])
    #     school.save()
    #     return render_template("student.html", student=student), 200  
    # else:
    #     return 400 



@app.route("/student/<string:student_id>/grades/add", methods=["POST"])
def add_a_grade(student_id):
    data = request.json
    school = School("./models/bcit.json")
    student = school.get_student(student_id)
    grade = data["grade"]
    
    # student = School.get_student(student_id)

    if "grade" not in data.keys():
        return 400 
    
    elif "grade" in data.keys():
        try:
            student.add_grade(grade)
        except ValueError:
            return "value error", 400 


        school.save()
        return render_template("student.html", student=student)

if __name__ == "__main__":
    app.run(debug=True) 