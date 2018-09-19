from flask import redirect, url_for, render_template
from flask import make_response, request, Blueprint
import flask
import requests, datetime, json
from app.models.user import User
import app as app_root


# Blueprint to create users and manage user list

user = Blueprint('user',__name__)

@user.route('/') #landing page redirects to --> list view 

def index():
    return redirect(url_for('.userlist'))

@user.route('/list') #list of users

def userlist():
    doc = User.objects()
    return render_template('user/index.html',users=doc)

@user.route('/create', methods=['POST','GET']) #create user 

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
                projectlist = (request.form['projects']).split(',')
                if '' in projectlist:
                    projectlist.remove('')
                userr.projects = projectlist 
            
            userr.save()  #save user details
            return redirect(url_for('.userlist')) #render user list view after saving
    
    return render_template('user/createuser.html') # rendering user creation form