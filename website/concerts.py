from flask import Blueprint, render_template

bp = Blueprint('concert', __name__, url_prefix='/details')

@bp.route('/concert')
def details():
    return render_template('templates/concert.html')