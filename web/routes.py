from flask import render_template,url_for, flash,redirect
from web import app
from web.forms import RegistrationForm, LoginForm
from web.models import User, Post

posts=[
        {
        'author':'Chris Maghas',
        'title':'Blog Post 1',
        'content':'Second Post Content',
        'date_posted':'April 22,2018'
        },
        {
        'author':'Rose Mwangi',
        'title':'Blog Post 2',
        'content':'Second Post Content',
        'date_posted':'April 22,2018'
        }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts,title='Demo')


@app.route("/about")
def about():
    return render_template('about.html',title='about')

@app.route("/feedback")
def feedback():
    return render_template('feedback.html',posts=posts,title='feedback')

@app.route("/reports")
def reports():
    return render_template('reports.html',title='View Coda Reports')

@app.route("/register", methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form=LoginForm()
    return render_template('login.html',title='Login',form=form)
