from flask import Flask, render_template


def create_app():
    """ Create and Config an instant of the flask appl."""
    app = Flask(__name__)


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
