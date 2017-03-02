import os
from flask import make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from model import Competitor


def generate(sport_duration, user_perf):
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
    if sport_duration != 'total_time':
        time = user_perf[sport_duration].total_seconds() / 3600
        user_feature = ['42', time]
    else:
        time = user_perf['swimming_time']
        time += user_perf['biking_time']
        time += user_perf['running_time']
        time = time.total_seconds() / 3600
        user_feature = ['42', time]
    features.append(user_feature)

    # sort
    features = sorted(features, key=lambda features: features[1])
    for feature in features:
        y.append(feature[1])

    # index of user feature
    user_index = features.index(user_feature)

    # generate y
    x = list(range(len(y)))

    axis.scatter(x, y, s=0.2)
    axis.scatter(x[user_index], y[user_index], color='black')
    # highlight one point
    import numpy as np
    axis.annotate('YOU: ' + str(user_index),
                  xy=(x[user_index], y[user_index]),
                  xytext=(x[user_index] * 0.5, y[user_index] * 0.8),
                  arrowprops=dict(facecolor='black', shrink=0.05))

    fig.suptitle(sport_duration)
    axis.set_xlabel('rank')
    axis.set_ylabel('duration (hours)')

    canvas = FigureCanvas(fig)
    path = os.path.join(os.path.dirname(__file__), 'assets/' + sport_duration + '.png')
    fig.savefig(path)
    return None
