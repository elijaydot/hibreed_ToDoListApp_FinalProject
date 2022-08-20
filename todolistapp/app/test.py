from datetime import date, datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from app import app
from app.models import Todo
from app import db

from routes import add

add()