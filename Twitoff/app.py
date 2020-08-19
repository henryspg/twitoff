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
        return render_template('base.html', title='Home')
        # return "hello twittersssss"

############################## addition #######################
    @app.route('/update')
    def update():
        #reset DB
        DB.drop_all()
        DB.create_all()
        insert_example_users()
        return render_template('base.html', title='Users updated!', users=User.query.all())

############################## end addition ###################


    return app
