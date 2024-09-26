from flask import Blueprint, render_template, request, redirect, url_for, flash

from DB import DB
from DB.models import User

user_bp = Blueprint('user', __name__)
db = DB()


@user_bp.route('/profile', methods=['GET'])
def profile():
    return render_template('my_profile.html')