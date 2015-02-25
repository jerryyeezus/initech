#!/bin/sh

host="http://localhost:8000/"
#host="http://ec2-54-69-18-202.us-west-2.compute.amazonaws.com:8000/"

http -f POST "$host""register/" name="Jerry Yee" email="yee@gatech.edu" password="asdf" confirm_password="asdf" user_type="INSTRUCTOR" skills_str="" > /dev/null

http -f POST "$host""register/" name="Bud Peterson" email="you@gatech.edu" password="pass" confirm_password="pass" user_type="INSTRUCTOR" skills_str="" > /dev/null

http -f POST "$host""register/" name="Thang Nguyen" email="thang@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="" > /dev/null

http -f POST "$host""add_courses/" course_name="Compilers" course_dept_and_id="CS 4240" course_professor="INSTRUCTOR|yee@gatech.edu"

http -f POST "$host""add_courses/" course_name="Networking" course_dept_and_id="CS 3251" course_professor="INSTRUCTOR|you@gatech.edu" > /dev/null


http -f POST "$host""add_courses/" course_name="Operating Systems" course_dept_and_id="CS 4210" course_professor="INSTRUCTOR|you@gatech.edu" > /dev/null

http -f POST "$host""add_import/" import_csv@roster.csv pk=3

http -f POST "$host""add_assignment/" assignment_number=1 course_fk=1
