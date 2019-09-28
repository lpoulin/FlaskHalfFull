from flask import render_template
from app import app

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