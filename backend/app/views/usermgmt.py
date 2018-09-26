from flask import redirect, url_for, render_template
from flask import request, Blueprint, flash
from app.models.user import User
from app.models.projects import Project
from app.views.forms import UserForm
from bson.objectid import ObjectId

# Blueprint to create users and manage user list

user = Blueprint('user', __name__)


@user.route('/')  # landing page redirects to --> list view
def index():
    return redirect(url_for('.userlist'))


@user.route('/list')  # list of users
def userlist():
    doc = User.objects()
    return render_template('user/index.html', users=doc)


@user.route('/create', methods=['POST', 'GET'])  # create user
def createuser():
    form = UserForm()
    projects = Project.objects()
    if projects():
        form.projects.choices = [(proj.id, proj.name) for proj in projects]
    if request.method == 'POST' and form.validate_on_submit():
        usr = User.objects(email=form.email.data).first()
        if usr:
            flash('User email already in use. Choose a different id!', 'danger')
        else:
            useer = User()
            useer.occupation = form.occupation.data
            useer.name = form.username.data
            useer.place = form.place.data
            useer.email = form.email.data
            useer.age = form.age.data
            t = request.form.to_dict(flat=False)
            if t.get('projects'):
                projs = [ObjectId(i) for i in t.get('projects')]
                useer.projects = projs
            useer.save()
            flash('User has been created successfully!', 'success')
            return redirect(url_for('.userlist'))  # render user list view after saving
    return render_template('user/createuser.html', form=form, legend='Create new users here.',
                           title='User Creation', operation='Create')  # rendering user creation form


@user.route('/user/<string:uid>')  #  User read
def showuser(uid):
    doc = User.objects.get_or_404(id=uid)
    if doc:
        return render_template('user/showuser.html', user=doc, projects=doc.projects)
    else:
        return redirect(url_for('user.userlist'))


@user.route('/user/<string:uid>/update', methods=["GET", "POST"])   #  User update
def modifyuser(uid):
    form = UserForm()
    projects = Project.objects()
    if projects():
        form.projects.choices = [(proj.id, proj.name) for proj in projects]
    doc = User.objects.get_or_404(id=uid)
    if form.validate_on_submit():
        user = User.objects(email=form.email.data).first()
        if proj and str(user.id) != str(uid):
            flash('email id already in use. Choose a different id for the project!', 'danger')
        else:
            doc.name = form.username.data
            doc.age = form.age.data
            doc.place = form.place.data
            doc.occupation = form.occupation.data
            doc.email = form.email.data
            t = request.form.to_dict(flat=False)
            if t.get('projects'):
                projs = [ObjectId(i) for i in t.get('projects')]
                doc.projects = projs
            else:
                doc.projects = []
            doc.save()
            flash('User updated successfully!', 'success')
            return redirect(url_for('user.userlist'))
    form.username.data = doc.name
    form.email.data = doc.email
    form.occupation.data = doc.occupation
    form.place.data = doc.place
    form.age.data = doc.age
    if len(doc.projects):
        form.projects.data = [t.id for t in doc.projects]
    return render_template('user/createuser.html', legend='Update your users here.',
                           title='User Updation', operation='Update', form=form)


@user.route('/user/<string:uid>/delete', methods=["GET"])
def deleteuser(uid):                                            # User delete
    try:
        User.objects.get(id=uid).delete()
        return redirect(url_for('user.userlist'))
    except:
        return render_template('Notfound.html')