from flask import render_template, redirect, url_for, current_app
from flask_sqlalchemy import get_debug_queries
from app.main import main

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('map.html')