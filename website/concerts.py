from flask import Blueprint, render_template
from .models import Concert, Comment
from flask_login import login_required, current_user
import os

bp = Blueprint('concert', __name__)

@bp.route('/concert')
def details():
    return render_template('concerts/show.html')

def check_upload_file(form):
    fp.form.image.data
    filename=fp.filename
    BASE_PATH=os.path.dirname(__file__)
    upload_path=os.path.join(BASE_PATH, 'static/img', secure_filename(filename))
    db_upload_path='/static/img' + secure_filename(filename)
    fp_save(upload_path)
    return db_upload_path