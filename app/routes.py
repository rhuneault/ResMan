from app import app
from flask import render_template
from app.objs.objects import Application

@app.route('/')
@app.route('/index')
def index():
    applications = [
        Application('TD', 'Analyst', 'Not applied'),
        Application('Manulife', 'Manager', 'Applied')
    ]
    return render_template('applications.html', applications=applications)
