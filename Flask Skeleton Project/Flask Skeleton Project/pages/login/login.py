from flask import Blueprint, request, redirect, url_for, session, render_template,sessions
from pymongo import MongoClient
from flask_login import login_user, logout_user, login_required, current_user
from collections import OrderedDict



# blueprint definition
login = Blueprint(
    'login',
    __name__,
    static_folder='static',
    static_url_path='/login',
    template_folder='templates'
)


# Routes
@login.route('/login', methods=['GET', 'POST'])
def index():
    if session.get('logged_in') == True:
        session['message'] = 'you are already signed in'
        return render_template('login.html')
    else:
        return render_template('login.html')

    ##### her  to addddd the relevant errors message
