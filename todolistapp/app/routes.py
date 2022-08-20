from datetime import date, datetime
from venv import create
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from app import app
from app.models import Todo
from app import db


@app.route('/')
def index():
	incomplete = Todo.query.filter_by(complete=False).all()
	complete = Todo.query.filter_by(complete=True).all()

	return render_template('index.html', incomplete=incomplete, complete=complete)


@app.route('/add', methods=['POST'])
def add():
	title = request.form['title']
	body = request.form['body']
	created_by = request.form['created_by']
	date_created = request.form['date_created']
	assigned_to = request.form['assigned_to']
	due_date = request.form['due_date']
	activity_duration = request.form['activity_duration']
	comment = request.form['comment']
	
	todo = Todo(title=title, body = body, created_by=created_by, date_created=date_created, assigned_to=assigned_to, due_date=due_date,  activity_duration=activity_duration, comment=comment, complete=False)

	db.session.add(todo)
	db.session.commit()

	return redirect(url_for('index'))


@app.route('/complete/<id>')
def complete(id):

	todo = Todo.query.filter_by(id=int(id)).first()
	todo.complete = True
	db.session.commit()

	return redirect(url_for('index'))

@app.route('/incomplete/<id>')
def incomplete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = False
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/view/<id>', methods=["GET", "POST"])
def viewnote(id):
	todo = Todo.query.filter_by(id=int(id)).first()
	if request.method == 'POST':
		if todo:
			todo.complete = False
    		# db.session.commit()
			return redirect(url_for('index'))

	return render_template('viewnote.html', todo = todo)



@app.route('/uncheck/<id>')
def uncheck(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
	todo = Todo.query.filter_by(id=int(id)).first()
	db.session.delete(todo)
	db.session.commit()
	return redirect(url_for('index'))

'''
# to request for confirmation before delete, call the delete.html. 
# Simple uncomment this section and coomment the other delete route.
@app.route('/delete/<id>')
def delete(id):
	todo = Todo.query.filter_by(id=int(id)).first()
	if request.method == 'POST':
		if todo:

			db.session.delete(todo)
			db.session.commit()
			return redirect('/delete')

	return render_template('delete.html', todo = todo)
'''

@app.route('/update/<id>', methods=["GET", "POST"])
def update(id):
	todo = Todo.query.filter_by(id=int(id)).first()
	if request.method == 'POST':
		if todo:
			
			db.session.delete(todo)
			db.session.commit()

			title = request.form['title']
			body = request.form['body']
			created_by = request.form['created_by']
			date_created = request.form['date_created']
			assigned_to = request.form['assigned_to']
			due_date = request.form['due_date']
			activity_duration = request.form['activity_duration']
			comment = request.form['comment']

			todo = Todo(title=title, body=body, created_by=created_by, date_created=date_created, assigned_to=assigned_to, due_date=due_date,  activity_duration=activity_duration, comment=comment, complete=False)
			
			db.session.add(todo)
			db.session.commit()
			# return redirect(f'/update/{id}')
			return redirect(url_for('index'))
		
		return f"Note with id = {id} Does not exist"

	# return redirect(url_for('index'))
	return render_template('update.html', todo = todo)



	'''
	id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.String(200))
    created_by = db.Column(db.String(30))
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    assigned_to = db.Column(db.String(30))  
    due_date = db.Column(db.DateTime(),  default=datetime.utcnow, onupdate=datetime.utcnow)
    activity_duration = db.Column(db.String(10))
    comment = db.Column(db.String(255))
    complete = db.Column(db.Boolean)
	'''