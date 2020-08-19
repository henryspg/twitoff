from flask import Flask, render_template
import sys


def create_app():
    app = Flask(__name__)


    ## TODO.........  make the app
    @app.route('/') # what??
    def route():
        print("Hello, about to return the root / route stuff", file=sys.stdout)
        return render_template('base.html', title='Homee')

    return app
