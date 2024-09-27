from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from DB import DB
from DB.models import Category, Product, Box, User

from blueprints import auth_bp, products_bp, user_bp

app = Flask(__name__)
db = DB()
login_manger = LoginManager(app)


app.config['SECRET_KEY'] = "aosdhaoishdoaisd"

login_manger.login_view = 'login'
with app.app_context():
    db.create_tables()

app.register_blueprint(auth_bp)
app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(user_bp, url_prefix='/')

@login_manger.user_loader
def load_user(user_id):
    return db.get_record(User, 'user_id', user_id)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/statistics')
def statistics():
    return render_template('statistics.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')