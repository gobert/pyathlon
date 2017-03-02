from setup import db


class Competitor(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(80))
    swimming_time = db.Column(db.Interval)
    biking_time   = db.Column(db.Interval)
    running_time  = db.Column(db.Interval)
    total_time    = db.Column(db.Interval)

    def __init__(self, competitor_data):
        self.id   = competitor_data['id']
        self.name = competitor_data['name']
        self.swimming_time = competitor_data['swimming']
        self.biking_time   = competitor_data['biking']
        self.running_time  = competitor_data['running']
        self.total_time    = competitor_data['total']

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def truncate(cls):
        for record in cls.query.all():
            db.session.delete(record)
        db.session.commit()

    def __repr__(self):
        return '<User %r>' % self.name
