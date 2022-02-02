from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mr. Johnson'}
    posts = [
        {
            'author': {'username': 'Dan'},
            'body': 'Beautiful day in Tahoe!'
        },
        {
            'author': {'username': 'Jade'},
            'body': 'We need more snow!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)