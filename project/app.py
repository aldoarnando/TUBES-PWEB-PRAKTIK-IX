from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# memuat file .env
load_dotenv()

# menginisialisasi aplikasi Flask
app = Flask(__name__)

# mendapatkan nilai dari variabel environment
app.secret_key = os.environ.get('SECRET_KEY')
HOST = os.environ.get('HOST')
PORT = int(os.environ.get('PORT'))
USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')
DB = os.environ.get('DB')
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = True


db = SQLAlchemy(app)
from project.models import Users, Diagnosis, BeratBadanUmur, TinggiBadanUmur, IndeksMassaTubuh
migrate = Migrate(app, db)