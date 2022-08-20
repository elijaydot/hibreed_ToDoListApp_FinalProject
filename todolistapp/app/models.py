from turtle import title
from app import db
from datetime import date, datetime


class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.Text(length=80))
  body = db.Column(db.Text(length=200))
  created_by = db.Column(db.Text(length=30))
  date_created = db.Column(db.Text)
  assigned_to = db.Column(db.Text(length=30))
  due_date = db.Column(db.Text)
  activity_duration = db.Column(db.Text(length=30))
  comment = db.Column(db.Text(length=255))
  complete = db.Column(db.Boolean)


'''
  def __init__(self, title, body, created_by, assigned_to, activity_duration, comment, complete):
    self.title = title
    self.body = body
    self.created_by = created_by
    self.assigned_to = assigned_to
    self.activity_duration = activity_duration
    self.comment = comment
    self.complete = complete
'''

'''
  id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.String(200))
    created_by = db.Column(db.String(30))
    date_created = db.Column(db.Date(), default=date.today)
    assigned_to = db.Column(db.String(30))  
    due_date = db.Column(db.Date(),  default=date.today, onupdate=date.today)
    activity_duration = db.Column(db.String(30))
    comment = db.Column(db.String(255))
    complete = db.Column(db.Boolean)



    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text(80))
    body = db.Column(db.Text(200))
    created_by = db.Column(db.Text(30))
    date_created = db.Column(db.Date(), default=date.today)
    assigned_to = db.Column(db.Text(30))  
    due_date = db.Column(db.Date(),  default=date.today, onupdate=date.today)
    activity_duration = db.Column(db.Text(30))
    comment = db.Column(db.Text(255))
    complete = db.Column(db.Boolean)

'''