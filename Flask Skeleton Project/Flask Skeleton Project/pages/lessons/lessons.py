from flask import render_template
from flask import Blueprint

#blueprint definition
lessons = Blueprint(
    'lessons',
    __name__,
    static_folder='static',
    static_url_path='/lessons',
    template_folder='templates'
)

# Routes
@lessons.route('/lessons')
def index():
    return render_template('lessons.html')
