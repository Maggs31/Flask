from flask import redirect, url_for, render_template, make_response, request, Blueprint
import flask
import os, requests, datetime, json
from app.models.user import User
import app as app_root
user = Blueprint('user',__name__, url_prefix='/users')

@user.route('/')
def index():
    return redirect(url_for('user.userlist'))

@user.route('/list')
def userlist():
    doc = User.objects()
    return render_template('user/index.html',users=doc)

@user.route('/create', methods=['POST','GET'])
def createuser():
    if request.method =='POST':
        name = request.form['username']   
        if not name:
            return "<html><body><h1>Can't create user without name</h1></div></body></html>" 
        else:
            userr = User()
            userr.name = name
            userr.occupation = request.form['occupation']
            if request.form['age']:
                userr.age = int(request.form['age'])
            userr.place = request.form['place']
            if request.form['projects']:
                userr.projects = (request.form['projects']).split(',')
            userr.save()
            return redirect(url_for('user.userlist'))
    return render_template('user/createuser.html')