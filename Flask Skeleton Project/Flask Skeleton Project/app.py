from flask import Flask
from flask import render_template, redirect, url_for, Blueprint, session, request, jsonify, flash
from datetime import datetime, date, time, timedelta

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.secret_key = '12345'
app.permanent_session_lifetime = timedelta(minutes=5)

###########################################################################
###########################################################################
#   # secret key : 12345

#   #  MongoDB :
       # username : jabrahaj2212@gmail.com
       # password : jabra12345
       #uri = "mongodb+srv://Prosport:Prosport123@cluster0.vztqxlp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#   # To start login try :
        #example1@example.com
        #Ex111111
########################################################################
########################################################################

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers

app.register_blueprint(page_error_handlers)

###### Components
## Main menu
from components.main_menu.main_menu import main_menu

app.register_blueprint(main_menu)

##### data base
from db_connector import db_connector

app.register_blueprint(db_connector)

###################### new routes #### Pages

##Mongo page just for trying and debuging
from pages.MongoDB.MongoDB import MongoDB
app.register_blueprint(MongoDB)

## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## About
from pages.about.about import about
app.register_blueprint(about)

## Profile
from pages.profile.profile import profile
app.register_blueprint(profile)

# login page
from pages.login.login import login
app.register_blueprint(login)

# register page
from pages.register.register import register
app.register_blueprint(register)

# edit information page
from pages.editinfo.editinfo import editinfo
app.register_blueprint(editinfo)

# lessons page
from pages.lessons.lessons import lessons
app.register_blueprint(lessons)

# booklesson page
from pages.booklesson.booklesson import booklesson
app.register_blueprint(booklesson)

from pages.viewbookings.viewbookings import viewbookings
app.register_blueprint(viewbookings)

###################

##         MONGO DB   -- all from MongoDB.py
## MongoDB page was made for debugginfg and check data base functionality
## So we can delete this page because we imported the data base also from db_connector
## To help the teacher checking our project we will keep MongoDB page and connectors

from pages.MongoDB.MongoDB import prosportDB

############################ routs and functions ###################################

#################### log in - log out

@app.route('/logout', methods=['GET'])
def logout_func():
    session['logged_in'] = False
    session['username'] = ''
    session['email'] = ''
    session['first_name'] = ''
    session['last_name'] = ''
    session['phone_number'] = ''
    session['message'] = ''
    session['booking_message'] = ''
    return redirect(url_for('homepage.index'))


@app.route('/logged_in', methods=['POST', 'GET'])
def login_account():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the user exists in the database and if the password matches
        user = prosportDB.accounts.find_one({'email': email, 'password': password})

        if user:
            # Log in the user
            session['email'] = email  # Store the email in the session
            session['logged_in'] = True
            session['message'] = 'great! successfully signed in'
            session['first_name'] = user.get('first_name')
            session['last_name'] = user.get('last_name')
            session['phone_number'] = user.get('phone_number')
            return redirect(url_for('profile.index'))  # Redirect to the profile page
        else:
            session['message'] = (' Cant log in, invalid email or password')
            return redirect(url_for('login.index'))


################## registeration

@app.route('/validate-register-account', methods=['POST', 'GET'])
def validate_register_account():
    if request.method == 'POST':
        email = request.get_json()['email']
        account = prosportDB.accounts.find_one({'email': email})
        if account:
            return jsonify({"user_exists": "true"})
    return jsonify({"user_exists": "false"})


from pages.register.register import validate_form
@app.route('/register-account', methods=['POST', 'GET'])
def register_account():
    if request.method == 'POST':
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        birthdate = request.form['birth_date']
        password = request.form['password']
        healthcertificant = request.form['health_certification']


        # Insert account data into DB if errors = true , it means no errors
        valid = validate_form(email, first_name, last_name, phone_number, birthdate, password)
        existing_email = prosportDB.accounts.find_one({'email': email})

        if existing_email:
            flash('Email already exists. Try to log in instead.', 'error')
            return redirect(url_for('register.index'))
        else:
            if valid:
                prosportDB.accounts.insert_one({
                    'email': email,
                    'first_name': first_name,
                    'last_name': last_name,
                    'phone_number': phone_number,
                    'birth_date': birthdate,
                    'password': password,
                    'health_certification': healthcertificant
                })
                session['message'] = 'Your account has been successfully registered, please log in to start your experience'
                return redirect(url_for('login.index'))
            else:
                flash('Please fill the data according to our suggestions', 'error')
                return redirect(url_for('register.index'))


######### updating account

@app.route('/update-account', methods=['POST', 'GET'])
def update_account():
    session['booking_message'] = ''
    session['message'] = ''
    if session.get('logged_in'):
        if request.method == 'POST':
            logged_in_email = session.get('email')
            user_data = prosportDB.accounts.find_one({'email': logged_in_email})
            session['message'] = ''

            if request.form.get('first_name'):
                first_name = request.form.get('first_name')
            else:
                first_name = user_data.get('first_name')
            if request.form.get('last_name'):
                last_name = request.form.get('last_name')
            else:
                last_name = user_data.get('last_name')
            if request.form.get('phone_number'):
                phone_number = request.form.get('phone_number')
            else:
                phone_number = user_data.get('phone_number')
            if request.form.get('birth_date'):
                birth_date = request.form.get('birth_date')
            else:
                birth_date = user_data.get('birth_date')
            if request.form.get('password'):
                password = request.form.get('password')
            else:
                password = user_data.get('password')
            if request.form.get('health_certification'):
                health = request.form.get('health_certification')
            else:
                health =''

            session['first_name'] = first_name
            session['last_name'] = last_name
            session['phone_number'] = phone_number

            valid = validate_form(logged_in_email, first_name, last_name, phone_number, birth_date, password)
            update_doc = {logged_in_email, first_name, last_name, phone_number, birth_date, password}
            if valid:
                prosportDB.accounts.update_one({'email': logged_in_email},
                                               {'$set': {'first_name': first_name
                                                   , 'last_name': last_name
                                                   , 'phone_number': phone_number
                                                   , 'birth_date': birth_date
                                                   , 'password': password
                                                ,'health_certification': health}
                                                })
                session['message'] = 'Your account has been updated'
                session['edit_message'] = ''
                return redirect(url_for('profile.index'))
            else:
                session['edit_message'] = 'One or more fields are invalid, please try again'
                return redirect(url_for('editinfo.index'))

        # If it's a GET request, just render the update account form
        return render_template('editinfo.html')



############# book new lesson

from pages.booklesson.booklesson import validate_booking_form

@app.route('/book_new_lesson', methods=['POST', 'GET'])
def book_new_lesson():
    session['booking_message'] = ''
    session['message'] = ''
    if request.method == 'POST':
        if session.get('logged_in'):
            logged_in_email = session.get('email')
            lesson_type = request.form['lesson_type']
            lesson_date = request.form['lesson_date']
            lesson_time = request.form['lesson_time']

            valid = validate_booking_form(lesson_type, lesson_date, lesson_time)
            if valid:
                prosportDB.bookings.insert_one({
                    'email': logged_in_email,
                    'Type': lesson_type,
                    'Date': lesson_date,
                    'Time': lesson_time
                })
                session['message'] = 'Congrats! Your booking has been created'
                return redirect(url_for('profile.index'))
            else:
                return redirect(url_for('booklesson.index'))


############### view bookings ## and canceling future ones
@app.route('/view_my_bookings', methods=['POST', 'GET'])
def view_my_bookings():
    if session.get('logged_in') == True:
        logged_in_email = session.get('email')
        my_all_bookings = list(prosportDB.bookings.find({'email': logged_in_email}))
        future_bookings = []
        past_bookings = []

        for booking in my_all_bookings:
            booking_date = datetime.strptime(booking['Date'], '%Y-%m-%d').date()
            if booking_date < datetime.now().date():
                past_bookings.append(booking)
            else:
                future_bookings.append(booking)
        future_bookings = sorted(future_bookings, key=lambda x: datetime.strptime(x['Date'], '%Y-%m-%d'))
        past_bookings = sorted(past_bookings, key=lambda x: datetime.strptime(x['Date'], '%Y-%m-%d'), reverse=True)

        return render_template('viewbookings.html', future_bookings=list(future_bookings), past_bookings=list(past_bookings))
    else:
        session['message'] = 'You are not signed in'
        return redirect(url_for('login.index'))


from bson.objectid import ObjectId

@app.route('/cancel_booking/<booking_id>', methods=['GET'])
def cancel_booking(booking_id):
    prosportDB.bookings.delete_one({'_id': ObjectId(booking_id)})
    return redirect(url_for('view_my_bookings'))
