from flask import Blueprint, render_template, request, redirect, url_for, flash
from App.controllers import create_staff, assign_staff_to_course, get_all_staff

staff_views = Blueprint('staff_views', __name__, template_folder='../templates')

@staff_views.route('/staff', methods=['GET'])
def get_staff_page():
    staff = get_all_staff()
    return render_template('staff.html', staff=staff)

@staff_views.route('/staff', methods=['POST'])
def create_staff_action():
    data = request.form
    create_staff(data['staff_name'], data['staff_role'])
    flash(f"Staff member {data['staff_name']} created!")
    return redirect(url_for('staff_views.get_staff_page'))

@staff_views.route('/staff/assign', methods=['POST'])
def assign_staff_action():
    data = request.form
    assign_staff_to_course(data['staff_id'], data['course_id'])
    flash(f"Assigned staff member {data['staff_id']} to course {data['course_id']}")
    return redirect(url_for('staff_views.get_staff_page'))