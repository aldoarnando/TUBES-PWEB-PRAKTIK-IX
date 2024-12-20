from flask import render_template, redirect, request
from project.app import app
from project.controllers.page import *
from project.templates import *

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['GET', 'POST'])
def cekStunting():
    if request.method == 'POST':
        return insertDiagnosis()
    return render_template('cek_stunting.html')