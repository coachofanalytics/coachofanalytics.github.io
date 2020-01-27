from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY']='5664f518db9744c8fbe7f1fdc398e9ca'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

from web import routes
