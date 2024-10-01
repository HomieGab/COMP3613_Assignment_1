from flask import Blueprint, render_template, request, redirect, url_for, flash
from App.controllers import create_course, get_all_courses, get_course_staff

course_views = Blueprint('course_views', __name__, template_folder='../templates')

@course_views.route('/courses', methods=['GET'])
def get_courses_page():
    courses = get_all_courses()
    return render_template('courses.html', courses=courses)

@course_views.route('/courses', methods=['POST'])
def create_course_action():
    data = request.form
    create_course(data['course_name'], data['course_code'])
    flash(f"Course {data['course_name']} created!")
    return redirect(url_for('course_views.get_courses_page'))

@course_views.route('/courses/<int:course_id>/staff', methods=['GET'])
def view_course_staff(course_id):
    staff = get_course_staff(course_id)
    return render_template('course_staff.html', staff=staff)