from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Concert

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    concerts=Concert.query.all()
    return render_template('index.html', concerts=concerts)


@bp.route('/search')
def search():
    if request.args['search']:
        print(request.args['search'])
        artist_search = "%" + request.args['search'] + '%'
        concerts = Concert.query.filter(Concert.name.like(artist_search)).all()
        return render_template('concerts/search.html', concerts=concerts)
    else:
        concerts=Concert.query.all()
        return render_template('index.html', concerts=concerts)