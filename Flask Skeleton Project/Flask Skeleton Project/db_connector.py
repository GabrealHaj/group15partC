from flask import Blueprint, render_template
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

#  blueprint definition
db_connector = Blueprint(
    'db_connector',
    __name__,
    static_folder='static',
    static_url_path='/db_connector',
    template_folder='templates'
)

uri = "mongodb+srv://Prosport:Prosport123@cluster0.vztqxlp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

cluster = MongoClient(uri, server_api=ServerApi('1'))
prosportDB = cluster['prosportDB']
accounts_col = prosportDB['accounts']
ourLessons_col = prosportDB['ourLessons']
bookings_col = prosportDB['bookings']


@db_connector.route('/db_connector')
def index():
    message = prosportDB.list_collection_names()

    accounts_list = list(accounts_col.find())
    lessons_list = list(ourLessons_col.find())
    bookings_list = list(bookings_col.find())

    return render_template('',
                           message=message, accounts_list=accounts_list, lessons_list=lessons_list
                           , bookings_list=bookings_list)
#
# # create all necessary functions
# def get_list_of_customers():
#     return list(customers_col.find())
#
#
# def insert_customer(customer_dict):
#     customers_col.insert_one(customer_dict)
#
# # ...
