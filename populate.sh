#!/bin/sh

if [ "$1" = "server" ]
then
	host="http://ec2-54-69-18-202.us-west-2.compute.amazonaws.com:8000/"
elif [ "$1" = "local" ]
then
	host="http://localhost:8000/"
else
	echo "ayy lmao"
	exit 0
fi


http -f POST "$host""register/" name="Jerry Yee" email="yee@gatech.edu" password="pass" confirm_password="pass" user_type="INSTRUCTOR" skills_str="" > /dev/null

http -f POST "$host""register/" name="Bud Peterson" email="you@gatech.edu" password="pass" confirm_password="pass" user_type="INSTRUCTOR" skills_str="" > /dev/null

http -f POST "$host""register/" name="Thang Nguyen" email="thang@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="Java, HCI" > /dev/null

http -f POST "$host""register/" name="Jameson Fuccboi" email="fuccboi@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="Java, Python, Machine Learning" > /dev/null

http -f POST "$host""register/" name="Kanye West" email="yeezy@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="Java, C, Web Dev, HTML" > /dev/null

http -f POST "$host""register/" name="Lil Wayne" email="weezy@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="HTML, Web Dev" > /dev/null

http -f POST "$host""register/" name="Sam Smith" email="smith@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="Python, PHP, Java" > /dev/null

http -f POST "$host""register/" name="John Lennon" email="lennon@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="HTML, Java, C, PHP, UI Design" > /dev/null

http -f POST "$host""register/" name="Ringo Starr" email="starr@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="Web Dev, HTML, CSS" > /dev/null

http -f POST "$host""register/" name="Paul McCartney" email="mccartney@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="PHP, Web Dev" > /dev/null

http -f POST "$host""register/" name="George Harrison" email="harrison@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="C, C++, Angular, JQuery" > /dev/null

http -f POST "$host""register/" name="Elton John" email="john@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="HTML, Java" > /dev/null

http -f POST "$host""register/" name="Anne Hathaway" email="hathaway@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="C#, Java, SQL, Django" > /dev/null

http -f POST "$host""register/" name="Daniel Day Lewis" email="lewis@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="SQL, Java, HTML, HCI, C++" > /dev/null

http -f POST "$host""register/" name="Mike Myers" email="myers@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="Java, Python, HTML, PHP, C, CSS, Angular, Django" > /dev/null

http -f POST "$host""register/" name="Vin Diesel" email="diesel@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="Wed Dev, HTML, JQuery" > /dev/null

http -f POST "$host""register/" name="Michelle Rodriguez" email="rodriguez@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="Distributed Systems, Web Dev, HTML" > /dev/null

http -f POST "$host""register/" name="Dwayne Johnson" email="johnson@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="HCI, Robotics, Web Dev, Java, HTML, PHP" > /dev/null

http -f POST "$host""register/" name="Paul Walker" email="walker@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="Web Dev, Java, HTML, Angular, Django, C++, Distributed Systems" > /dev/null

http -f POST "$host""register/" name="Justin Bieber" email="bieber@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="JQuery, Java, HTML, PHP, UI Design" > /dev/null

http -f POST "$host""register/" name="Lindsay Lohan" email="lohan@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="UI Design, Machine Learning, Java, HTML, PHP" > /dev/null

http -f POST "$host""register/" name="Brenda Lin" email="lin@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="Java, C++, HTML, CSS, Robotics, HCI" > /dev/null

http -f POST "$host""register/" name="Brittany Miles" email="miles@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="Web Dev, Data Science, SQL, Java, PHP, HTML, CSS" > /dev/null

http -f POST "$host""register/" name="Lindsay Purcell" email="purcell@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="Data Science, Robotics, HCI, Java, C++" > /dev/null

http -f POST "$host""register/" name="Kenny Marino" email="marino@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="Java, Robotics, HCI" > /dev/null

http -f POST "$host""register/" name="David Raji" email="raji@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="Web Dev, HTML, CSS" > /dev/null

http -f POST "$host""register/" name="Josh Garrick" email="garrick@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="PHP, JQuery, Angular, Django" > /dev/null

http -f POST "$host""register/" name="Tyler Meuter" email="meuter@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="JavaScript, HTML, CSS, Web Dev, HCI, UI Design" > /dev/null

http -f POST "$host""register/" name="Kara Pendley" email="pendley@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="JavaScript, UI Design" > /dev/null

http -f POST "$host""register/" name="Alexa Grzech" email="grzech@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="C#, SQL, PHP, Java, HTML, HCI" > /dev/null

http -f POST "$host""register/" name="Wyatt Bazrod" email="bazrod@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="Data Science, Distributed Systems, Angular, Java" > /dev/null

http -f POST "$host""register/" name="Arvind Narayan" email="narayan@gatech.edu" password="pass" confirm_password="pass" user_type="STUDENT" skills_str="Java, JavaScript, HTML, CSS, Data Science" > /dev/null



http -f POST "$host""add_courses/" course_name="Compilers" course_dept_and_id="CS 4240" course_professor="INSTRUCTOR|yee@gatech.edu" > /dev/null

http -f POST "$host""add_courses/" course_name="Networking" course_dept_and_id="CS 3251" course_professor="INSTRUCTOR|you@gatech.edu" > /dev/null


http -f POST "$host""add_courses/" course_name="Operating Systems" course_dept_and_id="CS 4210" course_professor="INSTRUCTOR|you@gatech.edu" > /dev/null

http -f POST "$host""add_import/" import_csv@roster.csv pk=2 > /dev/null

http -f POST "$host""add_assignment/" assignment_number=1 course_fk=2 > /dev/null

http -f POST "$host""add_team/" which_assignment=1 owner='INSTRUCTOR|you@gatech.edu'> /dev/null

http -f POST "$host""add_team/" which_assignment=1 owner='INSTRUCTOR|you@gatech.edu'> /dev/null

http -f POST "$host""add_team/" which_assignment=1 owner='INSTRUCTOR|you@gatech.edu'> /dev/null

http -f PUT "$host""add_team/" which_team=1 which_student='STUDENT|thang@gatech.edu' which_action='add' > /dev/null

http -f PUT "$host""add_team/" which_team=1 which_student='STUDENT|fuccboi@gatech.edu' which_action='add' > /dev/null

http -f PUT "$host""add_team/" which_team=2 which_student='STUDENT|yeezy@gatech.edu' which_action='add' > /dev/null


http -f PUT "$host""add_team/" which_team=3 which_student='PLACEHOLDER|joe@gatech.edu' which_action='add' > /dev/null

#questions for students

http -f POST "$host""questions/" ass_fk=1 hi='Very interested' lo='Not interested' text='Are you interested in web development?' > /dev/null

http -f POST "$host""questions/" ass_fk=1 hi='Very interested' lo='Not interested' text='Are you interested in app development?' > /dev/null

http -f POST "$host""questions/" ass_fk=1 hi='Very interested' lo='Not interested' text='Are you interested in data management?' > /dev/null

http -f POST "$host""questions/" ass_fk=1 hi='Very interested' lo='Not interested' text='Are you interested in front-end design?' > /dev/null

http -f POST "$host""questions/" ass_fk=1 hi='Very interested' lo='Not interested' text='Are you interested in data science?' > /dev/null

http -f POST "$host""questions/" ass_fk=1 hi='Very good' lo='Not good' text='How are your Java skills?' > /dev/null

http -f POST "$host""questions/" ass_fk=1 hi='Very good' lo='Not good' text='How are your HTML skills?' > /dev/null

http -f POST "$host""questions/" ass_fk=1 hi='Very good' lo='Not good' text='How are your C skills?' > /dev/null

http -f POST "$host""questions/" ass_fk=1 hi='Very good' lo='Not good' text='How are your PHP skills?' > /dev/null

http -f POST "$host""questions/" ass_fk=1 hi='Very good' lo='Not good' text='How are your Angular skills?' > /dev/null

#answers for students

http -f PUT "$host""answer/1/thang@gatech.edu/" question_fk=1 user_fk="STUDENT|thang@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/2/thang@gatech.edu/" question_fk=2 user_fk="STUDENT|thang@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/3/thang@gatech.edu/" question_fk=3 user_fk="STUDENT|thang@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/4/thang@gatech.edu/" question_fk=4 user_fk="STUDENT|thang@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/5/thang@gatech.edu/" question_fk=5 user_fk="STUDENT|thang@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/6/thang@gatech.edu/" question_fk=6 user_fk="STUDENT|thang@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/7/thang@gatech.edu/" question_fk=7 user_fk="STUDENT|thang@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/8/thang@gatech.edu/" question_fk=8 user_fk="STUDENT|thang@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/9/thang@gatech.edu/" question_fk=9 user_fk="STUDENT|thang@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/10/thang@gatech.edu/" question_fk=10 user_fk="STUDENT|thang@gatech.edu" value=1 weight=1 > /dev/null

http -f PUT "$host""answer/1/fuccboi@gatech.edu/" question_fk=1 user_fk="STUDENT|fuccboi@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/2/fuccboi@gatech.edu/" question_fk=2 user_fk="STUDENT|fuccboi@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/3/fuccboi@gatech.edu/" question_fk=3 user_fk="STUDENT|fuccboi@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/4/fuccboi@gatech.edu/" question_fk=4 user_fk="STUDENT|fuccboi@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/5/fuccboi@gatech.edu/" question_fk=5 user_fk="STUDENT|fuccboi@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/6/fuccboi@gatech.edu/" question_fk=6 user_fk="STUDENT|fuccboi@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/7/fuccboi@gatech.edu/" question_fk=7 user_fk="STUDENT|fuccboi@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/8/fuccboi@gatech.edu/" question_fk=8 user_fk="STUDENT|fuccboi@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/9/fuccboi@gatech.edu/" question_fk=9 user_fk="STUDENT|fuccboi@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/10/fuccboi@gatech.edu/" question_fk=10 user_fk="STUDENT|fuccboi@gatech.edu" value=1 weight=1 > /dev/null

http -f PUT "$host""answer/1/yeezy@gatech.edu/" question_fk=1 user_fk="STUDENT|yeezy@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/2/yeezy@gatech.edu/" question_fk=2 user_fk="STUDENT|yeezy@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/3/yeezy@gatech.edu/" question_fk=3 user_fk="STUDENT|yeezy@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/4/yeezy@gatech.edu/" question_fk=4 user_fk="STUDENT|yeezy@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/5/yeezy@gatech.edu/" question_fk=5 user_fk="STUDENT|yeezy@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/6/yeezy@gatech.edu/" question_fk=6 user_fk="STUDENT|yeezy@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/7/yeezy@gatech.edu/" question_fk=7 user_fk="STUDENT|yeezy@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/8/yeezy@gatech.edu/" question_fk=8 user_fk="STUDENT|yeezy@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/9/yeezy@gatech.edu/" question_fk=9 user_fk="STUDENT|yeezy@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/10/yeezy@gatech.edu/" question_fk=10 user_fk="STUDENT|yeezy@gatech.edu" value=1 weight=1 > /dev/null

http -f PUT "$host""answer/1/weezy@gatech.edu/" question_fk=1 user_fk="STUDENT|weezy@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/2/weezy@gatech.edu/" question_fk=2 user_fk="STUDENT|weezy@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/3/weezy@gatech.edu/" question_fk=3 user_fk="STUDENT|weezy@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/4/weezy@gatech.edu/" question_fk=4 user_fk="STUDENT|weezy@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/5/weezy@gatech.edu/" question_fk=5 user_fk="STUDENT|weezy@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/6/weezy@gatech.edu/" question_fk=6 user_fk="STUDENT|weezy@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/7/weezy@gatech.edu/" question_fk=7 user_fk="STUDENT|weezy@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/8/weezy@gatech.edu/" question_fk=8 user_fk="STUDENT|weezy@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/9/weezy@gatech.edu/" question_fk=9 user_fk="STUDENT|weezy@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/10/weezy@gatech.edu/" question_fk=10 user_fk="STUDENT|weezy@gatech.edu" value=1 weight=1 > /dev/null

http -f PUT "$host""answer/1/smith@gatech.edu/" question_fk=1 user_fk="STUDENT|smith@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/2/smith@gatech.edu/" question_fk=2 user_fk="STUDENT|smith@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/3/smith@gatech.edu/" question_fk=3 user_fk="STUDENT|smith@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/4/smith@gatech.edu/" question_fk=4 user_fk="STUDENT|smith@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/5/smith@gatech.edu/" question_fk=5 user_fk="STUDENT|smith@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/6/smith@gatech.edu/" question_fk=6 user_fk="STUDENT|smith@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/7/smith@gatech.edu/" question_fk=7 user_fk="STUDENT|smith@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/8/smith@gatech.edu/" question_fk=8 user_fk="STUDENT|smith@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/9/smith@gatech.edu/" question_fk=9 user_fk="STUDENT|smith@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/10/smith@gatech.edu/" question_fk=10 user_fk="STUDENT|smith@gatech.edu" value=2 weight=1 > /dev/null

http -f PUT "$host""answer/1/lennon@gatech.edu/" question_fk=1 user_fk="STUDENT|lennon@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/2/lennon@gatech.edu/" question_fk=2 user_fk="STUDENT|lennon@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/3/lennon@gatech.edu/" question_fk=3 user_fk="STUDENT|lennon@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/4/lennon@gatech.edu/" question_fk=4 user_fk="STUDENT|lennon@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/5/lennon@gatech.edu/" question_fk=5 user_fk="STUDENT|lennon@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/6/lennon@gatech.edu/" question_fk=6 user_fk="STUDENT|lennon@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/7/lennon@gatech.edu/" question_fk=7 user_fk="STUDENT|lennon@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/8/lennon@gatech.edu/" question_fk=8 user_fk="STUDENT|lennon@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/9/lennon@gatech.edu/" question_fk=9 user_fk="STUDENT|lennon@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/10/lennon@gatech.edu/" question_fk=10 user_fk="STUDENT|lennon@gatech.edu" value=1 weight=1 > /dev/null

http -f PUT "$host""answer/1/starr@gatech.edu/" question_fk=1 user_fk="STUDENT|starr@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/2/starr@gatech.edu/" question_fk=2 user_fk="STUDENT|starr@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/3/starr@gatech.edu/" question_fk=3 user_fk="STUDENT|starr@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/4/starr@gatech.edu/" question_fk=4 user_fk="STUDENT|starr@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/5/starr@gatech.edu/" question_fk=5 user_fk="STUDENT|starr@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/6/starr@gatech.edu/" question_fk=6 user_fk="STUDENT|starr@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/7/starr@gatech.edu/" question_fk=7 user_fk="STUDENT|starr@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/8/starr@gatech.edu/" question_fk=8 user_fk="STUDENT|starr@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/9/starr@gatech.edu/" question_fk=9 user_fk="STUDENT|starr@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/10/starr@gatech.edu/" question_fk=10 user_fk="STUDENT|starr@gatech.edu" value=1 weight=1 > /dev/null

http -f PUT "$host""answer/1/mccartney@gatech.edu/" question_fk=1 user_fk="STUDENT|mccartney@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/2/mccartney@gatech.edu/" question_fk=2 user_fk="STUDENT|mccartney@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/3/mccartney@gatech.edu/" question_fk=3 user_fk="STUDENT|mccartney@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/4/mccartney@gatech.edu/" question_fk=4 user_fk="STUDENT|mccartney@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/5/mccartney@gatech.edu/" question_fk=5 user_fk="STUDENT|mccartney@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/6/mccartney@gatech.edu/" question_fk=6 user_fk="STUDENT|mccartney@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/7/mccartney@gatech.edu/" question_fk=7 user_fk="STUDENT|mccartney@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/8/mccartney@gatech.edu/" question_fk=8 user_fk="STUDENT|mccartney@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/9/mccartney@gatech.edu/" question_fk=9 user_fk="STUDENT|mccartney@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/10/mccartney@gatech.edu/" question_fk=10 user_fk="STUDENT|mccartney@gatech.edu" value=2 weight=1 > /dev/null

http -f PUT "$host""answer/1/harrison@gatech.edu/" question_fk=1 user_fk="STUDENT|harrison@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/2/harrison@gatech.edu/" question_fk=2 user_fk="STUDENT|harrison@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/3/harrison@gatech.edu/" question_fk=3 user_fk="STUDENT|harrison@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/4/harrison@gatech.edu/" question_fk=4 user_fk="STUDENT|harrison@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/5/harrison@gatech.edu/" question_fk=5 user_fk="STUDENT|harrison@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/6/harrison@gatech.edu/" question_fk=6 user_fk="STUDENT|harrison@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/7/harrison@gatech.edu/" question_fk=7 user_fk="STUDENT|harrison@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/8/harrison@gatech.edu/" question_fk=8 user_fk="STUDENT|harrison@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/9/harrison@gatech.edu/" question_fk=9 user_fk="STUDENT|harrison@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/10/harrison@gatech.edu/" question_fk=10 user_fk="STUDENT|harrison@gatech.edu" value=4 weight=1 > /dev/null

http -f PUT "$host""answer/1/john@gatech.edu/" question_fk=1 user_fk="STUDENT|john@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/2/john@gatech.edu/" question_fk=2 user_fk="STUDENT|john@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/3/john@gatech.edu/" question_fk=3 user_fk="STUDENT|john@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/4/john@gatech.edu/" question_fk=4 user_fk="STUDENT|john@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/5/john@gatech.edu/" question_fk=5 user_fk="STUDENT|john@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/6/john@gatech.edu/" question_fk=6 user_fk="STUDENT|john@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/7/john@gatech.edu/" question_fk=7 user_fk="STUDENT|john@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/8/john@gatech.edu/" question_fk=8 user_fk="STUDENT|john@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/9/john@gatech.edu/" question_fk=9 user_fk="STUDENT|john@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/10/john@gatech.edu/" question_fk=10 user_fk="STUDENT|john@gatech.edu" value=1 weight=1 > /dev/null

http -f PUT "$host""answer/1/hathaway@gatech.edu/" question_fk=1 user_fk="STUDENT|hathaway@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/2/hathaway@gatech.edu/" question_fk=2 user_fk="STUDENT|hathaway@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/3/hathaway@gatech.edu/" question_fk=3 user_fk="STUDENT|hathaway@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/4/hathaway@gatech.edu/" question_fk=4 user_fk="STUDENT|hathaway@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/5/hathaway@gatech.edu/" question_fk=5 user_fk="STUDENT|hathaway@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/6/hathaway@gatech.edu/" question_fk=6 user_fk="STUDENT|hathaway@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/7/hathaway@gatech.edu/" question_fk=7 user_fk="STUDENT|hathaway@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/8/hathaway@gatech.edu/" question_fk=8 user_fk="STUDENT|hathaway@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/9/hathaway@gatech.edu/" question_fk=9 user_fk="STUDENT|hathaway@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/10/hathaway@gatech.edu/" question_fk=10 user_fk="STUDENT|hathaway@gatech.edu" value=3 weight=1 > /dev/null

http -f PUT "$host""answer/1/lewis@gatech.edu/" question_fk=1 user_fk="STUDENT|lewis@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/2/lewis@gatech.edu/" question_fk=2 user_fk="STUDENT|lewis@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/3/lewis@gatech.edu/" question_fk=3 user_fk="STUDENT|lewis@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/4/lewis@gatech.edu/" question_fk=4 user_fk="STUDENT|lewis@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/5/lewis@gatech.edu/" question_fk=5 user_fk="STUDENT|lewis@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/6/lewis@gatech.edu/" question_fk=6 user_fk="STUDENT|lewis@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/7/lewis@gatech.edu/" question_fk=7 user_fk="STUDENT|lewis@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/8/lewis@gatech.edu/" question_fk=8 user_fk="STUDENT|lewis@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/9/lewis@gatech.edu/" question_fk=9 user_fk="STUDENT|lewis@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/10/lewis@gatech.edu/" question_fk=10 user_fk="STUDENT|lewis@gatech.edu" value=1 weight=1 > /dev/null

http -f PUT "$host""answer/1/myers@gatech.edu/" question_fk=1 user_fk="STUDENT|myers@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/2/myers@gatech.edu/" question_fk=2 user_fk="STUDENT|myers@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/3/myers@gatech.edu/" question_fk=3 user_fk="STUDENT|myers@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/4/myers@gatech.edu/" question_fk=4 user_fk="STUDENT|myers@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/5/myers@gatech.edu/" question_fk=5 user_fk="STUDENT|myers@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/6/myers@gatech.edu/" question_fk=6 user_fk="STUDENT|myers@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/7/myers@gatech.edu/" question_fk=7 user_fk="STUDENT|myers@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/8/myers@gatech.edu/" question_fk=8 user_fk="STUDENT|myers@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/9/myers@gatech.edu/" question_fk=9 user_fk="STUDENT|myers@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/10/myers@gatech.edu/" question_fk=10 user_fk="STUDENT|myers@gatech.edu" value=4 weight=1 > /dev/null

http -f PUT "$host""answer/1/diesel@gatech.edu/" question_fk=1 user_fk="STUDENT|diesel@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/2/diesel@gatech.edu/" question_fk=2 user_fk="STUDENT|diesel@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/3/diesel@gatech.edu/" question_fk=3 user_fk="STUDENT|diesel@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/4/diesel@gatech.edu/" question_fk=4 user_fk="STUDENT|diesel@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/5/diesel@gatech.edu/" question_fk=5 user_fk="STUDENT|diesel@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/6/diesel@gatech.edu/" question_fk=6 user_fk="STUDENT|diesel@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/7/diesel@gatech.edu/" question_fk=7 user_fk="STUDENT|diesel@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/8/diesel@gatech.edu/" question_fk=8 user_fk="STUDENT|diesel@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/9/diesel@gatech.edu/" question_fk=9 user_fk="STUDENT|diesel@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/10/diesel@gatech.edu/" question_fk=10 user_fk="STUDENT|diesel@gatech.edu" value=1 weight=1 > /dev/null

http -f PUT "$host""answer/1/rodriguez@gatech.edu/" question_fk=1 user_fk="STUDENT|rodriguez@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/2/rodriguez@gatech.edu/" question_fk=2 user_fk="STUDENT|rodriguez@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/3/rodriguez@gatech.edu/" question_fk=3 user_fk="STUDENT|rodriguez@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/4/rodriguez@gatech.edu/" question_fk=4 user_fk="STUDENT|rodriguez@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/5/rodriguez@gatech.edu/" question_fk=5 user_fk="STUDENT|rodriguez@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/6/rodriguez@gatech.edu/" question_fk=6 user_fk="STUDENT|rodriguez@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/7/rodriguez@gatech.edu/" question_fk=7 user_fk="STUDENT|rodriguez@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/8/rodriguez@gatech.edu/" question_fk=8 user_fk="STUDENT|rodriguez@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/9/rodriguez@gatech.edu/" question_fk=9 user_fk="STUDENT|rodriguez@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/10/rodriguez@gatech.edu/" question_fk=10 user_fk="STUDENT|rodriguez@gatech.edu" value=1 weight=1 > /dev/null

http -f PUT "$host""answer/1/johnson@gatech.edu/" question_fk=1 user_fk="STUDENT|johnson@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/2/johnson@gatech.edu/" question_fk=2 user_fk="STUDENT|johnson@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/3/johnson@gatech.edu/" question_fk=3 user_fk="STUDENT|johnson@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/4/johnson@gatech.edu/" question_fk=4 user_fk="STUDENT|johnson@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/5/johnson@gatech.edu/" question_fk=5 user_fk="STUDENT|johnson@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/6/johnson@gatech.edu/" question_fk=6 user_fk="STUDENT|johnson@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/7/johnson@gatech.edu/" question_fk=7 user_fk="STUDENT|johnson@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/8/johnson@gatech.edu/" question_fk=8 user_fk="STUDENT|johnson@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/9/johnson@gatech.edu/" question_fk=9 user_fk="STUDENT|johnson@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/10/johnson@gatech.edu/" question_fk=10 user_fk="STUDENT|johnson@gatech.edu" value=3 weight=1 > /dev/null

http -f PUT "$host""answer/1/walker@gatech.edu/" question_fk=1 user_fk="STUDENT|walker@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/2/walker@gatech.edu/" question_fk=2 user_fk="STUDENT|walker@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/3/walker@gatech.edu/" question_fk=3 user_fk="STUDENT|walker@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/4/walker@gatech.edu/" question_fk=4 user_fk="STUDENT|walker@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/5/walker@gatech.edu/" question_fk=5 user_fk="STUDENT|walker@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/6/walker@gatech.edu/" question_fk=6 user_fk="STUDENT|walker@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/7/walker@gatech.edu/" question_fk=7 user_fk="STUDENT|walker@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/8/walker@gatech.edu/" question_fk=8 user_fk="STUDENT|walker@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/9/walker@gatech.edu/" question_fk=9 user_fk="STUDENT|walker@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/10/walker@gatech.edu/" question_fk=10 user_fk="STUDENT|walker@gatech.edu" value=4 weight=1 > /dev/null

http -f PUT "$host""answer/1/bieber@gatech.edu/" question_fk=1 user_fk="STUDENT|bieber@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/2/bieber@gatech.edu/" question_fk=2 user_fk="STUDENT|bieber@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/3/bieber@gatech.edu/" question_fk=3 user_fk="STUDENT|bieber@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/4/bieber@gatech.edu/" question_fk=4 user_fk="STUDENT|bieber@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/5/bieber@gatech.edu/" question_fk=5 user_fk="STUDENT|bieber@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/6/bieber@gatech.edu/" question_fk=6 user_fk="STUDENT|bieber@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/7/bieber@gatech.edu/" question_fk=7 user_fk="STUDENT|bieber@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/8/bieber@gatech.edu/" question_fk=8 user_fk="STUDENT|bieber@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/9/bieber@gatech.edu/" question_fk=9 user_fk="STUDENT|bieber@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/10/bieber@gatech.edu/" question_fk=10 user_fk="STUDENT|bieber@gatech.edu" value=1 weight=1 > /dev/null

http -f PUT "$host""answer/1/lohan@gatech.edu/" question_fk=1 user_fk="STUDENT|lohan@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/2/lohan@gatech.edu/" question_fk=2 user_fk="STUDENT|lohan@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/3/lohan@gatech.edu/" question_fk=3 user_fk="STUDENT|lohan@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/4/lohan@gatech.edu/" question_fk=4 user_fk="STUDENT|lohan@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/5/lohan@gatech.edu/" question_fk=5 user_fk="STUDENT|lohan@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/6/lohan@gatech.edu/" question_fk=6 user_fk="STUDENT|lohan@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/7/lohan@gatech.edu/" question_fk=7 user_fk="STUDENT|lohan@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/8/lohan@gatech.edu/" question_fk=8 user_fk="STUDENT|lohan@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/9/lohan@gatech.edu/" question_fk=9 user_fk="STUDENT|lohan@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/10/lohan@gatech.edu/" question_fk=10 user_fk="STUDENT|lohan@gatech.edu" value=1 weight=1 > /dev/null

http -f PUT "$host""answer/1/lin@gatech.edu/" question_fk=1 user_fk="STUDENT|lin@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/2/lin@gatech.edu/" question_fk=2 user_fk="STUDENT|lin@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/3/lin@gatech.edu/" question_fk=3 user_fk="STUDENT|lin@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/4/lin@gatech.edu/" question_fk=4 user_fk="STUDENT|lin@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/5/lin@gatech.edu/" question_fk=5 user_fk="STUDENT|lin@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/6/lin@gatech.edu/" question_fk=6 user_fk="STUDENT|lin@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/7/lin@gatech.edu/" question_fk=7 user_fk="STUDENT|lin@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/8/lin@gatech.edu/" question_fk=8 user_fk="STUDENT|lin@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/9/lin@gatech.edu/" question_fk=9 user_fk="STUDENT|lin@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/10/lin@gatech.edu/" question_fk=10 user_fk="STUDENT|lin@gatech.edu" value=2 weight=1 > /dev/null

http -f PUT "$host""answer/1/miles@gatech.edu/" question_fk=1 user_fk="STUDENT|miles@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/2/miles@gatech.edu/" question_fk=2 user_fk="STUDENT|miles@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/3/miles@gatech.edu/" question_fk=3 user_fk="STUDENT|miles@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/4/miles@gatech.edu/" question_fk=4 user_fk="STUDENT|miles@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/5/miles@gatech.edu/" question_fk=5 user_fk="STUDENT|miles@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/6/miles@gatech.edu/" question_fk=6 user_fk="STUDENT|miles@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/7/miles@gatech.edu/" question_fk=7 user_fk="STUDENT|miles@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/8/miles@gatech.edu/" question_fk=8 user_fk="STUDENT|miles@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/9/miles@gatech.edu/" question_fk=9 user_fk="STUDENT|miles@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/10/miles@gatech.edu/" question_fk=10 user_fk="STUDENT|miles@gatech.edu" value=2 weight=1 > /dev/null

http -f PUT "$host""answer/1/purcell@gatech.edu/" question_fk=1 user_fk="STUDENT|purcell@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/2/purcell@gatech.edu/" question_fk=2 user_fk="STUDENT|purcell@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/3/purcell@gatech.edu/" question_fk=3 user_fk="STUDENT|purcell@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/4/purcell@gatech.edu/" question_fk=4 user_fk="STUDENT|purcell@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/5/purcell@gatech.edu/" question_fk=5 user_fk="STUDENT|purcell@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/6/purcell@gatech.edu/" question_fk=6 user_fk="STUDENT|purcell@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/7/purcell@gatech.edu/" question_fk=7 user_fk="STUDENT|purcell@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/8/purcell@gatech.edu/" question_fk=8 user_fk="STUDENT|purcell@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/9/purcell@gatech.edu/" question_fk=9 user_fk="STUDENT|purcell@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/10/purcell@gatech.edu/" question_fk=10 user_fk="STUDENT|purcell@gatech.edu" value=1 weight=1 > /dev/null

http -f PUT "$host""answer/1/marino@gatech.edu/" question_fk=1 user_fk="STUDENT|marino@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/2/marino@gatech.edu/" question_fk=2 user_fk="STUDENT|marino@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/3/marino@gatech.edu/" question_fk=3 user_fk="STUDENT|marino@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/4/marino@gatech.edu/" question_fk=4 user_fk="STUDENT|marino@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/5/marino@gatech.edu/" question_fk=5 user_fk="STUDENT|marino@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/6/marino@gatech.edu/" question_fk=6 user_fk="STUDENT|marino@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/7/marino@gatech.edu/" question_fk=7 user_fk="STUDENT|marino@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/8/marino@gatech.edu/" question_fk=8 user_fk="STUDENT|marino@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/9/marino@gatech.edu/" question_fk=9 user_fk="STUDENT|marino@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/10/marino@gatech.edu/" question_fk=10 user_fk="STUDENT|marino@gatech.edu" value=1 weight=1 > /dev/null

http -f PUT "$host""answer/1/raji@gatech.edu/" question_fk=1 user_fk="STUDENT|raji@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/2/raji@gatech.edu/" question_fk=2 user_fk="STUDENT|raji@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/3/raji@gatech.edu/" question_fk=3 user_fk="STUDENT|raji@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/4/raji@gatech.edu/" question_fk=4 user_fk="STUDENT|raji@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/5/raji@gatech.edu/" question_fk=5 user_fk="STUDENT|raji@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/6/raji@gatech.edu/" question_fk=6 user_fk="STUDENT|raji@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/7/raji@gatech.edu/" question_fk=7 user_fk="STUDENT|raji@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/8/raji@gatech.edu/" question_fk=8 user_fk="STUDENT|raji@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/9/raji@gatech.edu/" question_fk=9 user_fk="STUDENT|raji@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/10/raji@gatech.edu/" question_fk=10 user_fk="STUDENT|raji@gatech.edu" value=1 weight=1 > /dev/null

http -f PUT "$host""answer/1/garrick@gatech.edu/" question_fk=1 user_fk="STUDENT|garrick@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/2/garrick@gatech.edu/" question_fk=2 user_fk="STUDENT|garrick@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/3/garrick@gatech.edu/" question_fk=3 user_fk="STUDENT|garrick@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/4/garrick@gatech.edu/" question_fk=4 user_fk="STUDENT|garrick@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/5/garrick@gatech.edu/" question_fk=5 user_fk="STUDENT|garrick@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/6/garrick@gatech.edu/" question_fk=6 user_fk="STUDENT|garrick@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/7/garrick@gatech.edu/" question_fk=7 user_fk="STUDENT|garrick@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/8/garrick@gatech.edu/" question_fk=8 user_fk="STUDENT|garrick@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/9/garrick@gatech.edu/" question_fk=9 user_fk="STUDENT|garrick@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/10/garrick@gatech.edu/" question_fk=10 user_fk="STUDENT|garrick@gatech.edu" value=5 weight=1 > /dev/null

http -f PUT "$host""answer/1/meuter@gatech.edu/" question_fk=1 user_fk="STUDENT|meuter@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/2/meuter@gatech.edu/" question_fk=2 user_fk="STUDENT|meuter@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/3/meuter@gatech.edu/" question_fk=3 user_fk="STUDENT|meuter@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/4/meuter@gatech.edu/" question_fk=4 user_fk="STUDENT|meuter@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/5/meuter@gatech.edu/" question_fk=5 user_fk="STUDENT|meuter@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/6/meuter@gatech.edu/" question_fk=6 user_fk="STUDENT|meuter@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/7/meuter@gatech.edu/" question_fk=7 user_fk="STUDENT|meuter@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/8/meuter@gatech.edu/" question_fk=8 user_fk="STUDENT|meuter@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/9/meuter@gatech.edu/" question_fk=9 user_fk="STUDENT|meuter@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/10/meuter@gatech.edu/" question_fk=10 user_fk="STUDENT|meuter@gatech.edu" value=1 weight=1 > /dev/null

http -f PUT "$host""answer/1/pendley@gatech.edu/" question_fk=1 user_fk="STUDENT|pendley@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/2/pendley@gatech.edu/" question_fk=2 user_fk="STUDENT|pendley@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/3/pendley@gatech.edu/" question_fk=3 user_fk="STUDENT|pendley@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/4/pendley@gatech.edu/" question_fk=4 user_fk="STUDENT|pendley@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/5/pendley@gatech.edu/" question_fk=5 user_fk="STUDENT|pendley@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/6/pendley@gatech.edu/" question_fk=6 user_fk="STUDENT|pendley@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/7/pendley@gatech.edu/" question_fk=7 user_fk="STUDENT|pendley@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/8/pendley@gatech.edu/" question_fk=8 user_fk="STUDENT|pendley@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/9/pendley@gatech.edu/" question_fk=9 user_fk="STUDENT|pendley@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/10/pendley@gatech.edu/" question_fk=10 user_fk="STUDENT|pendley@gatech.edu" value=1 weight=1 > /dev/null

http -f PUT "$host""answer/1/grzech@gatech.edu/" question_fk=1 user_fk="STUDENT|grzech@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/2/grzech@gatech.edu/" question_fk=2 user_fk="STUDENT|grzech@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/3/grzech@gatech.edu/" question_fk=3 user_fk="STUDENT|grzech@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/4/grzech@gatech.edu/" question_fk=4 user_fk="STUDENT|grzech@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/5/grzech@gatech.edu/" question_fk=5 user_fk="STUDENT|grzech@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/6/grzech@gatech.edu/" question_fk=6 user_fk="STUDENT|grzech@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/7/grzech@gatech.edu/" question_fk=7 user_fk="STUDENT|grzech@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/8/grzech@gatech.edu/" question_fk=8 user_fk="STUDENT|grzech@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/9/grzech@gatech.edu/" question_fk=9 user_fk="STUDENT|grzech@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/10/grzech@gatech.edu/" question_fk=10 user_fk="STUDENT|grzech@gatech.edu" value=1 weight=1 > /dev/null

http -f PUT "$host""answer/1/bazrod@gatech.edu/" question_fk=1 user_fk="STUDENT|bazrod@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/2/bazrod@gatech.edu/" question_fk=2 user_fk="STUDENT|bazrod@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/3/bazrod@gatech.edu/" question_fk=3 user_fk="STUDENT|bazrod@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/4/bazrod@gatech.edu/" question_fk=4 user_fk="STUDENT|bazrod@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/5/bazrod@gatech.edu/" question_fk=5 user_fk="STUDENT|bazrod@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/6/bazrod@gatech.edu/" question_fk=6 user_fk="STUDENT|bazrod@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/7/bazrod@gatech.edu/" question_fk=7 user_fk="STUDENT|bazrod@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/8/bazrod@gatech.edu/" question_fk=8 user_fk="STUDENT|bazrod@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/9/bazrod@gatech.edu/" question_fk=9 user_fk="STUDENT|bazrod@gatech.edu" value=1 weight=1 > /dev/null
http -f PUT "$host""answer/10/bazrod@gatech.edu/" question_fk=10 user_fk="STUDENT|bazrod@gatech.edu" value=5 weight=1 > /dev/null

http -f PUT "$host""answer/1/narayan@gatech.edu/" question_fk=1 user_fk="STUDENT|narayan@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/2/narayan@gatech.edu/" question_fk=2 user_fk="STUDENT|narayan@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/3/narayan@gatech.edu/" question_fk=3 user_fk="STUDENT|narayan@gatech.edu" value=4 weight=1 > /dev/null
http -f PUT "$host""answer/4/narayan@gatech.edu/" question_fk=4 user_fk="STUDENT|narayan@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/5/narayan@gatech.edu/" question_fk=5 user_fk="STUDENT|narayan@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/6/narayan@gatech.edu/" question_fk=6 user_fk="STUDENT|narayan@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/7/narayan@gatech.edu/" question_fk=7 user_fk="STUDENT|narayan@gatech.edu" value=5 weight=1 > /dev/null
http -f PUT "$host""answer/8/narayan@gatech.edu/" question_fk=8 user_fk="STUDENT|narayan@gatech.edu" value=2 weight=1 > /dev/null
http -f PUT "$host""answer/9/narayan@gatech.edu/" question_fk=9 user_fk="STUDENT|narayan@gatech.edu" value=3 weight=1 > /dev/null
http -f PUT "$host""answer/10/narayan@gatech.edu/" question_fk=10 user_fk="STUDENT|narayan@gatech.edu" value=2 weight=1 > /dev/null
