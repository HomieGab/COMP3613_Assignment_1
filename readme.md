# Software Engineering II (COMP3613) Assignment 1
#### Student Information:
* Student Name: Isaiah Gabriel Rambhajan
* Student ID: 816032612
* Course Name: Software Engineering II
* Assignment: COMP3613 Assignment 1


# Dependencies
* Python3/pip3
* Packages listed in requirements.txt

# Installing Dependencies
```bash
$ pip install -r requirements.txt
```

# Supported Commands:
* Create Course
```bash
flask course create 'course_name' 'course_code'
```
* Create Staff
```bash
flask staff create 'staff_name' 'staff_ID' 

* Assign staff
```bash
flask staff assign 'staff_ID' 'courseID'

* View Course Staff
```bash
flask get_course_staff 'courseID'

#