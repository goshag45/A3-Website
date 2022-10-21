from flask import Blueprint, render_template

bp = Blueprint('details', __name__)

@bp.route('/details')
def details():
    return render_template('templates/details.html')