from flask import Flask, render_template, request, send_from_directory
# from flask_sqlalchemy import SQLAlchemy
from setup import db

from model import Competitor
import graph_generator as generator
import importer
import helper
app = Flask(__name__)


@app.route("/import")
def import_results():
    importer.import_results()
    return 'done'


@app.route("/view")
def view_results():
    user_perf = {
        'swimming_time': helper.parse_date(request.args.get('swimming_time')),
        'biking_time': helper.parse_date(request.args.get('biking_time')),
        'running_time': helper.parse_date(request.args.get('running_time'))
    }

    response = generator.generate('swimming_time', user_perf)
    response = generator.generate('biking_time', user_perf)
    response = generator.generate('running_time', user_perf)
    response = generator.generate('total_time', user_perf)

    return render_template("results.html")


@app.route("/")
def hello():
    return render_template("index.html")


@app.route('/assets/<path:path>')
def send_asset(path):
    return send_from_directory('assets', path)


# init: db
db.create_all()


if __name__ == "__main__":
    print("DB initialization test: " + str(Competitor.query.count()))
    app.run()
