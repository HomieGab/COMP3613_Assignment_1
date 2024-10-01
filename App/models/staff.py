from App.database import db

class Staff(db.Model):
    staffID = db.Column(db.Integer, primary_key=True)
    staff_name = db.Column(db.String(120), nullable=False)
    staff_role = db.Column(db.String(50), nullable=False)  

    def __init__(self, staffID, staff_name, staff_role):
        self.set_staffID(staffID)
        self.set_staff_role(staff_role)
        self.set_staff_role(staff_role)
    
    def set_staffID(self, staffID):
        self.staffID = staffID
    
    def set_staff_name (self, staff_name):
        self.staff_name = staff_name

    def set_staff_role (self, staff_role):
        self.staff_role = staff_role