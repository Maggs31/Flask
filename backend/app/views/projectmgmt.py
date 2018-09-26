from flask import redirect, url_for, render_template
from flask import request, Blueprint, flash
from app.models.projects import Project
from app.views.forms import ProjectForm

# Blueprint to create projects and manage project list

project = Blueprint('project', __name__, url_prefix='/project')


@project.route('/list')  # list of projects
def projectlist():
    doc = Project.objects()
    return render_template('project/projectlist.html', projects=doc)


@project.route('/create', methods=['POST', 'GET'])  # create project
def createproject():
    form = ProjectForm()
    if form.validate_on_submit():
        proj = Project.objects(project_id=request.form['project_id']).first()
        if proj:
            flash('Project id already in use. Choose a different id!', 'danger')
        else:
            proj = Project()
            proj.project_id = request.form['project_id']
            proj.name = request.form['name']
            proj.type = request.form['type']
            proj.description = request.form['description']
            proj.save()
            flash('Project has been created successfully!', 'success')
            return redirect(url_for('project.projectlist'))  # render project list view after saving
    return render_template('project/createproject.html', legend='Create new projects here.',
                           title='Project Creation',operation='Create', form=form)  # rendering project creation form


@project.route('/<string:pid>')
def showproject(pid):
    doc = Project.objects.get_or_404(id=pid)
    if doc:
        return render_template('project/showproject.html', project=doc)


@project.route('/<string:pid>/update', methods=["GET", "POST"])
def modifyproject(pid):
    form = ProjectForm()
    doc = Project.objects(id=pid).first()
    print "Validation status", form.validate_on_submit()
    if form.validate_on_submit():
        proj = Project.objects(project_id=form.project_id.data).first()
        if proj and str(proj.id) != str(pid):
            flash('Project id already in use. Choose a different id for the project!', 'danger')
        else:
            doc.name = form.name.data
            doc.project_id = form.project_id.data
            doc.description = form.description.data
            doc.type = form.type.data
            doc.save()
            flash('Project updated!', 'success')
            return redirect(url_for('project.projectlist'))
    form.name.data = doc.name
    form.project_id.data = doc.project_id
    form.description.data = doc.description
    form.type.data = doc.type
    return render_template('project/createproject.html', legend='Update your projects here.',
                           title='Project Updation', operation='Update', form=form)


@project.route('/<string:pid>/delete', methods=["GET"])
def deleteproject(pid):  # delete an existing project
    try:
        Project.objects.get(id=pid).delete()
        return redirect(url_for('project.projectlist'))
    except:
        flash('Something went wrong', 'danger')
        return redirect(url_for(project.projectlist))