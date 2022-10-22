from flask import Blueprint, render_template

bp = Blueprint('concert', __name__)

@bp.route('/concert')
def details():
    return render_template('concerts/show.html')