from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'guy'}
    posts = [
        {
            'author': {'username': 'liam'},
            'body': 'i like to pass the ball to the other team'
        },
        {
            'author': {'username': 'dillon'},
            'body': 'i like to drive backwards'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title = 'Sign In', form=form)