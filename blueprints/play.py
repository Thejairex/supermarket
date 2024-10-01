from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
import sqlalchemy
from DB import DB
from DB.models import Days

play_bp = Blueprint('play', __name__)
db = DB()

@play_bp.route('/', methods=['GET', 'POST'])
@login_required
def play():
    if request.method == 'POST':
        money_start = float(request.form['money_start'])
        money_end = float(request.form['money_end'])
        day = Days(
            day = "Day " + str(request.form['day']),
            money_start = money_start,
            money_end = money_end,
            profit = money_end - money_start,
            user_id = current_user.user_id
        )
        try: 
            db.add(day)
            flash(f'Add {day.day} successful', 'success')
            return redirect(url_for('play.play'))
        
        except sqlalchemy.exc.IntegrityError as e:
            e = str(e)
            if 'UNIQUE constraint failed: days.day, days.user_id' in e:
                flash(f'The {day.day} already register', 'error')
            else:
                flash('Error al agregar Categoría {e}', 'error')
                
            db.rollback()
            return redirect(url_for('play.play'))
    # days = db.query(Days).filter_by(user_id = current_user.user_id).all()
    days = db.get_where(Days, 'user_id', current_user.user_id, order_by='day', order='desc')
    return render_template('play.html', days=days)

