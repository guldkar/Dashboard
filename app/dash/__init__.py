import os
from . import dash, db, models
from flask import Flask


def create_app(test_config =None):
    app = Flask(__name__, instance_relative_config =True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'dash.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config-py', silent=True)
    else:
        app.config.from_pyfile('config.py', silent=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)




    @app.route('/')
    def index():
        return dash.show_values()

    @app.route('/update/<field>/<time>')
    def update(field,time):

        update = dash.get_field_data(field, time)
        print("sending: ", update)
        return str(update)

    return app