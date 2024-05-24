import os
from flask import Flask, request, render_template, redirect, sessions, url_for
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User
from lib.space import *
from lib.space_repository import *

# Create a new Flask app
app = Flask(__name__)

@app.route('/home')
def get_home():
    return render_template('/home.html')

@app.route('/spaces', methods=['POST'])
def create_a_new_space():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)

# Access form data on the page using 
    name = request.form.get('name', '')
    description = request.form.get('description', '')
    price = request.form.get('price', '')
    user_id = 7 #PLACEHOLDER
    fromdate = request.form.get('fromdate', '')
    todate = request.form.get('todate', '')
    
    space = Space(None, description, price, user_id, name, fromdate, todate, free_dates=[])
    repository.add(space)

    return 'Listing added' #this probably does not return this message

@app.route('/spaces')
def get_spaces():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    spaces = repo.all()
    return render_template('/spaces.html', spaces=spaces)

@app.route('/home', methods=['POST'])
def create_user():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    
    user = User(None, request.form['new_username'], request.form['new_password'])

    repo.create(user)
    return redirect('/spaces')

@app.route('/add_new_property')
def get_new_listing_page():
    return render_template('/add_new_property.html')

@app.route('/spaces')
def filter_spaces_by_date():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    fromdate = request.args.get['fromdate']
    todate = request.args.get['todate']

    space_ids = repo.filter(fromdate, todate)


    return render_template('/spaces.html', space_ids=space_ids)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
