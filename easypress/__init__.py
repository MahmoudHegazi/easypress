#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from flask import Flask,abort,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

import os
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Theme, User, Page, Post
from flask import session as login_session
import random
import string

# IMPORTS FOR THIS STEP
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
import sqlite3
from flask import make_response
import requests
from flask import Flask, render_template, request



UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'js', 'css'}

app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




APPLICATION_NAME = "easypress"


# Connect to Database and create database session
engine = create_engine('sqlite:///easypress.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



@app.route('/theme/<filename>', methods = ['GET'])
def them(filename):
    return render_template('theme.html',filename=filename)




def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/add_theme/', methods = ['GET', 'POST'])
def add_theme(filename = None):
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # select the path for store file (control where to upload the file)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_url = str(app.config['UPLOAD_FOLDER']) + str(filename)
            return redirect(url_for('them',
                                    filename=filename))
    return render_template("upload_theme_form.html")



# App Interface
@app.route('/')
@app.route('/admin/', methods=['GET', 'POST'])
def wpAdmin():
    #if request.method == 'POST':
    return render_template('wp_admin.html')


"""
def get_page_url(userid):
    connection = sqlite3.connect("easypress.db")
    # cursor object
    crsr = connection.cursor()
    # execute the command to fetch the Sum of users likes from vote
    crsr.execute("SELECT Page.url FROM Page WHERE Page.page_creator = %s" %userid)
    # store the fetched data in the ans variable
    ans = crsr.fetchone()
    # store the sum of likes in virable ans[0] first index in the row
    page_url = ans[0]
    return page_url

def get_them_url(userid):
    connection = sqlite3.connect("easypress.db")
    # cursor object
    crsr = connection.cursor()
    # execute the command to fetch the Sum of users likes from vote
    crsr.execute("SELECT User.theme_id FROM User WHERE User.id = %s" %userid)
    # store the fetched data in the ans variable
    ans = crsr.fetchone()
    # store the sum of likes in virable ans[0] first index in the row
    them_id = ans[0]
    crsr.execute("SELECT Theme.url FROM Theme WHERE Theme.id = %s" %them_id)
    ans = crsr.fetchone()
    them_url = ans[0]
    return them_url


def select_theme(userid, theme_id):
    connection = sqlite3.connect("easypress.db")
    # cursor object
    crsr = connection.cursor()
    # execute the command to fetch the Sum of users likes from vote
    crsr.execute("UPDATE User SET Them.theme_id=theme_id WHERE User.id=userid;")
    # store the fetched data in the ans variable
    ans = crsr.fetchone()
    # store the sum of likes in virable ans[0] first index in the row
    return True

     count_likes = sumlikes()
     count_dislikes = sumdislikes()

"""


if __name__ == '__main__':
    app.secret_key = 'AS&S^1234Aoshsheo152h23h5j7ks9-1---3*-s,#k>s'
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)
