from App.models import Course, db

def create_course(course_name, course_code):
    newcourse = Course(course_name=course_name, course_code=course_code)
    db.session.add(newcourse)
    db.session.commit()
    return newcourse

def get_course(course_id):
    return Course.query.get(course_id)

def get_all_courses():
    return Course.query.all()

def get_course_staff(course_id):
    course = Course.query.get(course_id)
    return course.staff if course else []