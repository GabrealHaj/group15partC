from flask import render_template
from flask import Blueprint, session
from datetime import datetime, time

# blueprint definition
booklesson = Blueprint(
    'booklesson',
    __name__,
    static_folder='static',
    static_url_path='/booklesson',
    template_folder='templates'
)


# Routes
@booklesson.route('/booklesson')
def index():
    if session.get('logged_in'):
        return render_template('booklesson.html')
    else:
        session['message'] = 'Please log in to book a lesson'
        return render_template('login.html')


def validate_booking_form(lesson_type, lesson_date_str, lesson_time_str):
    lesson_date = datetime.strptime(lesson_date_str, '%Y-%m-%d').date()
    if lesson_date < datetime.now().date():
        session['booking_message'] = "Can't book a lesson on this date, Please try future date"
        return False
    else:
        lesson_time = datetime.strptime(lesson_time_str, '%H:%M').time()
        start_time = time(8, 0)  # 8 AM
        end_time = time(21, 0)  # 9 PM
        # Check if lesson_time is within bounds
        if not (start_time <= lesson_time <= end_time):
            session['booking_message'] = "Can't book a lesson at this ordered time. our working hours 8:00 - 21:00"
            return False
        else:
            session['booking_message'] = ''
            return True
