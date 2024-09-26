from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from DB import DB
from DB.models import User

db = DB()

auth_bp = Blueprint('auth', __name__)
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = db.get_by_column(User, 'username', request.form['username'])
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            flash('Login successful', 'success')
            
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        user = db.get_by_column(User, 'username', username)
        if user:
            flash('Username already exists', 'error')
            return redirect(url_for('auth.signup'))

        user = User(
            username = username,
            password = generate_password_hash(request.form['password']),
            role     = "user"
        )
        
        db.add(user)
        flash('Signup successful. Please login', 'success')
        return redirect(url_for('auth.login'))

    return render_template('signup.html')