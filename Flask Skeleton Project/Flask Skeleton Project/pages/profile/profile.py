
from flask import render_template, redirect, url_for, Blueprint, session, request



# homepage blueprint definition
profile = Blueprint(
    'profile',
    __name__,
    static_folder='static',
    static_url_path='/profile',
    template_folder='templates'
)


# Routes
@profile.route('/profile')
def index():
    if session.get('logged_in'):
        email = session.get('email')
        return render_template('profile.html', email=email)
    else:
        session['message'] = 'login required'
        return render_template('login.html')