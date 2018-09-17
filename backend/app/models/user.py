from app.extentions import db
from bson.objectid import ObjectId
from datetime import datetime

class User(db.Document):
	name = db.StringField(max_length=120, required=True) #real_name
	occupation = db.StringField()
	age = db.IntField()
	place = db.StringField()
	projects = db.ListField(db.StringField())
	created_at = db.DateTimeField(default=datetime.now())