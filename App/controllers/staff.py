from App.models import Staff, Course, db

#Assigns role eg. lecturer/TA/Tutor to staff
def create_staff(staff_name, staff_role):
    newstaff = Staff(staff_name=staff_name, staff_role=staff_role)
    db.session.add(newstaff)
    db.session.commit()
    return newstaff

def assign_staff_to_course(staff_id, course_id):
    staff = Staff.query.get(staff_id)
    course = Course.query.get(course_id)
    if staff and course:
        course.staff.append(staff)
        db.session.commit()

def get_all_staff():
    return Staff.query.all()