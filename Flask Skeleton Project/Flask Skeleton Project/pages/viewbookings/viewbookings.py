from flask import Blueprint,session
from flask import render_template, redirect, url_for


# homepage blueprint definition
viewbookings = Blueprint(
    'viewbookings',
    __name__,
    static_folder='static',
    static_url_path='/viewbookings',
    template_folder='templates'
)


# Routes
@viewbookings.route('/viewbookings')
def index():
    logged_in = session.get('logged_in')
    if logged_in:
        email = session.get('email')
        return render_template('viewbookings.html', email=email)
    else:
        session['message']='log in required'
        return render_template('login.html')

