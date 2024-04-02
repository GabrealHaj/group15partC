
from flask import Blueprint, render_template
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


# about blueprint definition
MongoDB = Blueprint(
    'MongoDB',
    __name__,
    static_folder='static',
    static_url_path='/MongoDB',
    template_folder='templates'
)

uri = "mongodb+srv://Prosport:Prosport123@cluster0.vztqxlp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

cluster = MongoClient(uri, server_api=ServerApi('1'))
prosportDB = cluster['prosportDB']
accounts_col = prosportDB['accounts']
ourLessons_col = prosportDB['ourLessons']
bookings_col = prosportDB['bookings']

# Routes
@MongoDB.route('/MongoDB')
def index():
    #message = 'Hello MongoDB!'
    #message = pymongo.version

    message = prosportDB.list_collection_names()

    accounts_list = list(accounts_col.find())
    lessons_list = list(ourLessons_col.find())
    bookings_list = list(bookings_col.find()) # her we can split it to future and past bookings

    return render_template('MongoDB.html',
                           message=message , accounts_list=accounts_list, lessons_list=lessons_list
                           , bookings_list= bookings_list)


