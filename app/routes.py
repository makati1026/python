from app import app
from flask import render_template, flash, redirect
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

# 'flash' functions returns message to user, since we aren't connected to a DB.
# Flask stores the message, but flashed messages will not magically appear in web pages. 
# The templates of the application need to render these flashed messages

# 'redirect()' function instructs the browser to navigate to a different page

