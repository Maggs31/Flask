from app.extentions import db
from datetime import datetime

#model for project
Choices = ('Individual Project', 'Team Project', 'Undecided')


class Project(db.Document):
    project_id = db.StringField(max_length=10, required=True, unique=True)
    name = db.StringField(max_length=40, required=True)
    description = db.StringField(required=True)
    type = db.StringField(choices=Choices, required=True)
    created_at = db.DateTimeField(default=datetime.now())
