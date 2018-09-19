from flask import redirect, url_for, render_template
from flask import make_response, request, Blueprint
import flask
from app.models.user import User
import app as app_root

#Blueprint for handling user delete, update and view requests

userconsole = Blueprint('userconsole',__name__, url_prefix='/user')

@userconsole.route('/<string:uid>',methods=["GET","POST"])

def index(uid):
	
	try:
		doc = User.objects.get(id=uid)
		
		if not doc:
			return render_template('Notfound.html')
	except:
		return render_template('Notfound.html')
	
	if request.method == 'GET': #displays user details update form
		return render_template('user/updateuser.html',user=doc)
	
	elif request.method == 'POST': #updates an existing user details
		name = request.form['username']   
		
		if not name:
			return render_template('Notfound.html') 
		
		else:
			doc.name = name
			doc.occupation = request.form['occupation']
			
			if request.form['age']:
				doc.age = int(request.form['age'])
			doc.place = request.form['place']
			
			if request.form['projects']:
				doc.projects = (request.form['projects']).split(',')
			doc.save()
			
			docs = User.objects()
			return redirect(url_for('user.userlist'))
			
@userconsole.route('/<string:uid>/delete',methods=["GET"])

def deleteuser(uid): #delete an existing user
	
	try:
		User.objects.get(id=uid).delete()
		docs = User.objects()
		return redirect(url_for('user.userlist'))
		
	except:
		return render_template('Notfound.html')