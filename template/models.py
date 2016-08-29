from tournament import app, db


class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, index=True, unique=True)
    email = db.Column(db.String, index=True)
    objects = db.relationship(
        'Object', backref='user', lazy='dynamic', cascade='all, delete-orphan'
    )

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def is_admin(self):
        return self.id in app.config["ADMIN_USERS"]

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User {}>'.format(self.id)


class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Object {}>'.format(self.name)
