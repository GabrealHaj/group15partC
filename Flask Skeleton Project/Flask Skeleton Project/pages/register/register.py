from flask import Blueprint, render_template, request, redirect, url_for,flash
# from ...pages.MongoDB.MongoDB import prosportDB
import re
from datetime import datetime

# blueprint definition
register = Blueprint(
    'register',
    __name__,
    static_folder='static',
    static_url_path='/register',
    template_folder='templates'
)


# Routes
@register.route('/register', methods=['GET', 'POST'])
def index():
    # Render registration form
    return render_template('register.html')


def validate_first_name(first_name):
    if not first_name.isalpha():
        print("First name should contain only letters.")
        return False
    else:
        return True


def validate_last_name(last_name):
    if not last_name.isalpha():
        print("Last name should contain only letters.")
        return False
    else:
        return True


def validate_phone_number(phone_number):
    if not re.match(r'^05\d{8}$', phone_number):
        flash('Your age should be at least 18', 'message')
        return False
    else:
        return True


def validate_birth_date(birth_date):
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    if datetime.now().year - birth_date.year < 18:
        print("Should be at least 18 years old.")
        return False
    else:
        return True


def validate_email(email):
    if not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email):
        print("Invalid email format.")
        return False
    else:
        return True


def validate_password(password):
    messages = []
    if len(password) < 8:
        messages.append("Password should be at least 8 characters long.")
    if not any(char.isdigit() for char in password):
        messages.append("Password should contain at least one digit (0-9).")
    if not any(char.islower() for char in password):
        messages.append("Password should contain at least one lowercase letter (a-z).")
    if not any(char.isupper() for char in password):
        messages.append("Password should contain at least one uppercase letter (A-Z).")
    if len(messages) > 0:
        return False
    else:
        return True


def validate_form(email, first_name, last_name, phone_number, birth_date, password):
    if (validate_email(email) and validate_first_name(first_name) and validate_last_name(last_name)
            and validate_password(password) and validate_phone_number(phone_number) and validate_birth_date(
                birth_date)):
        return True
    else:
        return False
