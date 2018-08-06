import os
import datetime
import pymysql
from flask import Flask
from flask import Flask, render_template, request, json, url_for,redirect, session, escape
from datetime import timedelta
import pymysql
from dotenv import load_dotenv, find_dotenv
#from werkzeug import generate_password_hash, check_password_hash
load_dotenv(find_dotenv())

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
# Connect to the database
username = os.getenv('C9_USER')

connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='recipe')
                             
connection = pymysql.connect(host='mysql://b58cd4f430707b:8e2fe11b@eu-cdbr-west-02.cleardb.net/heroku_ad06e2c54e075ba?reconnect=true',
                             user=username,
                             password='',
                             db='recipe')                             
                             

"""To ensure that sessions used timedout in 30 minutes of inactivities"""
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)


# Connect to the database
#connection = pymysql.connect(host='localhost', user="si_user",password="si_allow_pass_through", db='recipe')
"""Function to validate login for all pages available when a user is logged in"""
def validate_login():
    try:
        if session["email"] and session["password"]:   
            return 1
        else:
            return 0 
    except:
        return 0 
        

""" Update database Function"""
def update_database(sql_stm):
    rows = 0
    try:
        with connection.cursor() as cursor:
            rows = cursor.execute(sql_stm)
            connection.commit()
    except:
        ""
    return rows
    
    
"""The function is used to return one row only"""
def fetch_one_row(sql_stm):
    data = []
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            rows = cursor.execute(sql_stm)
            data = cursor.fetchone()
            connection.commit()
            if rows > 0:
               return data
            else:
               return data
    except:
        ""

"""The function is used to return all rows"""
def fetch_all_rows(sql_stm):
    data = []
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            rows = cursor.execute(sql_stm)
            data = cursor.fetchall()
            connection.commit()
            if rows > 0:
               return data
            else:
               return data
    except:
        ""        


"""Check if the email address is registered already"""    
def does_user_exist(email):
    try:
        with connection.cursor() as cursor:
            sql_stm = "SELECT * FROM authors WHERE email='"+ email +"';"
            rows = cursor.execute(sql_stm)
            connection.commit()
            if rows > 0:
               return True
            else:
               return False
    except:
        ""