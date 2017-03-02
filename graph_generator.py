
from flask import make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import StringIO
from model import Competitor


def generate(sport_duration):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    features = []
    x = []
    y = []
    for c in Competitor.query.all():
        # Delete Outliers
        duration = getattr(c, sport_duration).total_seconds()
        if duration != 0:
            time = float(duration) / 3600
            features.append([c.id, time])

    # add time of the user
    user_feature = ['42', 3.133333334]
    features.append(user_feature)

    # sort
    features = sorted(features, key=lambda features: features[1])
    for feature in features:
        y.append(feature[1])
    # y = sorted(y, key=lambda y: y)

    # index of user feature
    user_index = features.index(user_feature)

    # generate y
    x = list(range(len(y)))

    axis.scatter(x, y, s=0.2)
    axis.scatter(x[user_index], y[user_index], color='black')

    # highlight one point
    import numpy as np
    axis.annotate('Maxim: ' + str(user_index),
                  xy=(x[user_index], y[user_index]),
                  xytext=(x[user_index] * 0.5, y[user_index] * 0.8),
                  arrowprops=dict(facecolor='black', shrink=0.05))

    fig.suptitle('Triathlon Berlin 2016 - Olympic Distance')
    axis.set_xlabel('rank')
    axis.set_ylabel('duration (hours)')

    canvas = FigureCanvas(fig)
    output = StringIO.StringIO()
    canvas.print_png(output)
    return make_response(output.getvalue())
