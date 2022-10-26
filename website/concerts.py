from flask import Blueprint, render_template
from .models import Concert, Comment

bp = Blueprint('concert', __name__)

@bp.route('/concert')
def details():
    return render_template('concerts/show.html')