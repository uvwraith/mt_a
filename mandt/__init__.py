from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from mandt.main.routes import page_not_found

app = Flask(__name__)
app.register_error_handler(404, page_not_found)

app.secret_key = "edeacda59ac156398eb419c6b1ba496a5b8d0250cbf6f09299"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

admin = Admin(app, name='microblog', template_mode='bootstrap3')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username

class Others(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    for_username = db.Column(db.String(120), nullable=False)
    ssn = db.Column(db.String(120), nullable=False)
    dob = db.Column(db.String(120), nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.ssn

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    for_username = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.password

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Email, db.session))
admin.add_view(ModelView(Others, db.session))

from mandt.main.routes import main
from mandt.portals.routes import portals

app.register_blueprint(main)
app.register_blueprint(portals)