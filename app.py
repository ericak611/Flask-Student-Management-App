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

@app.route("/student/<string:student_id>/grades/add", methods=["POST"])
def add_a_grade(student_id):
    data = request.json
    school = School("./models/bcit.json")
    student = school.get_student(student_id)
    grade = data["grade"]

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