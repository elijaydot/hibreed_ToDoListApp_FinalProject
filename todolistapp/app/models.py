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
