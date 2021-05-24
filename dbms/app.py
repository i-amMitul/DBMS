from flask import Flask, render_template, jsonify, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, static_url_path = '', static_folder = 'templates')

app.config['SECRET_KEY'] = 'dbmsproject'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://User.sqlite3'

db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)