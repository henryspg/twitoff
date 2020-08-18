from flask import Flask, render_template


def create_app():
    app = Flask(__name__)


    ## TODO.........  make the app
    @app.route('/') # what??
    def route():
        return render_template('base.html', title='Home')

    return app
