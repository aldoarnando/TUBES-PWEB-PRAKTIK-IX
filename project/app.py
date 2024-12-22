from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from groq import Groq
import os

# memuat file .env
load_dotenv()

# menginisialisasi aplikasi Flask
app = Flask(__name__)

# mendapatkan nilai dari variabel environment
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
HOST = os.environ.get('HOST')
PORT = int(os.environ.get('PORT'))
USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')
DB = os.environ.get('DB')
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = True

# gunakan groq_api_key masing-masing
if not GROQ_API_KEY:
    raise ValueError("Masukan GROQ API KEY ke environment masing-masing atau pake hardcoded version.")
client = Groq(api_key=GROQ_API_KEY)

# membuat db sqlalchemy
db = SQLAlchemy(app)

# import model database
from project.models import Users, Diagnosis, BeratBadanUmur, TinggiBadanUmur, IndeksMassaTubuh

# inisialisasi migrate
migrate = Migrate(app, db)

# routing
from project.controllers.page import insertData, indexPage

@app.route("/")
def index():
    return indexPage()

@app.route("/cekstunt", methods=['GET', 'POST'])
def cekStunt():
    return insertData()