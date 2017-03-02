from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from setup import db

from model import Competitor
import graph_generator as generator
import importer

app = Flask(__name__)


@app.route("/import")
def import_results():
    importer.import_results()
    return 'done'


@app.route("/view")
def view_results():
    response = generator.generate('total_time')  # biking_time, running_time, total_time
    response.mimetype = 'image/png'
    return response


@app.route("/")
def hello():
    return "Hello World!"


# init: db
db.create_all()


if __name__ == "__main__":
    print("DB initialization test: " + str(Competitor.query.count()))
    app.run()
