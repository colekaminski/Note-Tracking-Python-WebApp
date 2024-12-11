
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash   #hashes the password so it doesn't store the actual password
from flask_login import login_user, login_required, logout_user, current_user

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    #Contains all data that is sent as a form, how we pull data from the server
    #data=request.form
    #print(data)
    #Adding variables inside here is how you can pass them to html pages
    #return render_template("login.html", text="Testing", user="COLE K", boolean=True)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #filter all users who have this email, returns first result
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):    #checks hashed password on server against user entered password
                flash('Logged in succesfully!!!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again!', category='error')
        else:
            flash('Email does not exist', category='error')
    return render_template("login.html", user=current_user)

@auth_bp.route('/logout')
@login_required     #cannot access this page unless user is logged in
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
    #return "<h1>LOGGING OUT</h1>"

@auth_bp.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(first_name) < 2:
            flash('Name must be > 2 chars', category='error')
        elif password1 != password2:
            flash('Passwords must match', category='error')
        else:
            #defines new user
            new_user = User(
                email=email, 
                first_name=first_name, 
                password=generate_password_hash(password1))
            #assigns new user to DB
            db.session.add(new_user)
            #commit changes
            db.session.commit()
            flash('Account created!', category='success')
            login_user(user, remember=True)
            #redirect user to home page (blueprint name.page name)
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)

###     BASIC ROTING W/ HEADING DISPLAYS
# @auth_bp.route('/login')
# def login():
#     return "<h1>AUTHORIZING</h1>"

# @auth_bp.route('/logout')
# def logout():
#     return "<h1>LOGGING OUT</h1>"

# @auth_bp.route('/sign-up')
# def sign_up():
#     return "<h1>CREATE AN ACCOUNT!!!</h1>"