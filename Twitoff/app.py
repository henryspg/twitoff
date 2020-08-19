from flask import Flask, render_template
from .models import *
# from twitoff.twitter import insert_example_users
from twitoff.twitter import *


def create_app():
    """ Create and Config an instant of the flask appl."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    ## TODO.........  make the app
    @app.route('/') # what??
    def root():
        print("hi?")
        return render_template('base.html', title='Hoome')
        # return "hello twittersssss"

############################## addition #######################
    @app.route('/update')
    def update():
        #reset DB
        print("just entered the update() function")
        DB.drop_all()
        print("just did drop_all")
        DB.create_all()
        print("just did create_all")
        insert_example_users()
        print("just did insert_example_users - app-py")
        return render_template('base.html', title='Users updated!', users=User.query.all())

############################## end addition ###################


    return app
