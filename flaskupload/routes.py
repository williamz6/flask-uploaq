from flask import  request, redirect, url_for, render_template, flash, session, current_app
from flaskupload import app, mysql, db, bcrypt
from flaskupload.data import Articles
from passlib.hash import sha256_crypt
from flaskupload.forms import RegForm, LoginForm
from flaskupload.models import User
from wtforms import Form
from flask_login import login_user, current_user, logout_user, login_required
from functools import wraps

@app.route('/')
@app.route('/anon')
def anon():
    return redirect(url_for('login'))


# register user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=RegForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, username=form.username.data, email=form.email.data, password=hashed_password)

        db.session.add(user)
        db.session.commit()

        flash('Your Account has been created', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form, title='Register')
        
        
# login form
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        admin= User.query.filter_by(email=form.email.data).first()
        if admin and bcrypt.check_password_hash(admin.password, form.password.data):
            login_user(admin, remember=form.remember.data)

            # next_page= request.args.get('next')
            return redirect(url_for('index'))
        else:
            error= "Invalid Login"
            return render_template('login.html', title='login', form=form, error=error)
    return render_template('login.html',title='login', form=form)    

# check if user logged in
# def is_logged_in(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             flash('Unauthorized user, Please login', 'danger')
#             return redirect(url_for('login'))
#     return wrap

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('anon'))

# homepage
@app.route('/index')
@login_required
def index():

    # cur = mysql.connection.cursor()
    users= User.query.all()
    if users:
        return render_template('index.html', title= 'home', users=users)
    else:
        msg= "No user found in database"
        return render_template('/index', title= 'home')


# display users
@app.route('/regusers')
@login_required
def regusers():

    
    users= User.query.all()

    if users:
        return render_template('users.html', users=users, title= 'view users')
    else:
        error= "blaj"
        return render_template('users.html', title= 'view users', error=error)

if __name__ == '__main__':
   
    app.run(debug=True)