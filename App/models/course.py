from App.database import db

class Course(db.Model):
    courseID = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(120), nullable=False)
    course_code = db.Column(db.String(10), nullable=False, unique=True)
    staff = db.relationship('Staff', secondary='course_staff', backref='courses')

class CourseStaff(db.Model):
    __tablename__ = 'course_staff'
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), primary_key=True)

    def __init__(self, courseID, course_name, course_code, staff):
        self.set_courseID(courseID)
        self.set_course_name(course_name)
        self.set_course_code(course_code)
        self.set_staff(staff)
    
    def set_courseID (self, courseID):
        self.courseID = courseID
    
    def set_course_name (self, course_name):
        self.course_name = course_name

    def set_course_code (self,  course_code):
        self.course_code = course_code

    def set_staff (self,  staff):
        self.staff = staff