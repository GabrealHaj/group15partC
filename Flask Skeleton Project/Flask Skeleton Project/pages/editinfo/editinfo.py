from flask import Blueprint,session
from flask import render_template, redirect, url_for


# homepage blueprint definition
editinfo = Blueprint(
    'editinfo',
    __name__,
    static_folder='static',
    static_url_path='/editinfo',
    template_folder='templates'
)


# Routes
@editinfo.route('/editinfo')
def index():
    logged_in = session.get('logged_in')
    if logged_in:
        email = session.get('email')
        return render_template('editinfo.html', email=email)
    else:
        session['message'] = 'login required'
        return render_template('login.html')


