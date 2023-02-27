# Student Management App with Flask 

## Project details 
In this project, a web application was built to allow visitors to view a list of students in a given school as well as view and manage their grades and GPA. Also an API was built so that we can interact with students and grades.

### Run Application
1. Run `python app.py`
2. In the browser, visit http://127.0.0.1:5000

### View List of Students and Their Grades
1. In the browser, visit http://127.0.0.1:5000
2. Click on the name of the student you wish to view.
3. This will bring you to a page with the student's name and their grades.

### To View a Student by Student ID
1. In the broswer, visit http://127.0.0.1:5000/student/<student_id>
    e.g., to view a student with the ID - A00000000
          visit http://127.0.0.1:5000/student/A00000000 

### API Endpoint - Add a Grade
*Data is expected to be passed as JSON*\
*Data must contain the following keys:*\
`grade`: grade of student

In an api testing tool like Postman, make a POST request with the appropriate key to http://127.0.0.1:5000/student/<student_id>/grades/add


### API Endpoint - Create a Student
*Data is expected to be passed as JSON*\
*Data must contain the following keys:*\
`name`: name of the student
`student_id`: student ID of student 

In an api testing tool like Postman, make a POST request with the appropriate keys to http://127.0.0.1:5000/student/add