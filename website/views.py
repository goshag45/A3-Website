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
        print("I AM HERE HELLOOOOOOO")
        search_query = "%" + request.args['search'] + '%'
        concerts = Concert.query.filter(Concert.name.like(search_query)).all()
        # Don't know what I'm doing here, just testing
        if request.option != 'select a genre':
            concerts_genre = Concert.query.filter(Concert.genre.data.like(search_query)).all()
        else:
            print("it is not working. sorry")
        #concerts = Concert.query.filter(Concert.city.like(search_query)).all()
        return render_template('concerts/search.html', concerts=concerts, concerts_genre=concerts_genre)
    else:
        concerts=Concert.query.all()
        return render_template('index.html', concerts=concerts)
# @bp.route('/search')
# def search():
#     if request.args['search']:
#         print(request.args['search'])
#         print("I AM HERE HELLOOOOOOO")
#         search_query = "%" + request.args['search'] + '%'
#         concerts = Concert.query.filter(Concert.name.like(search_query)).all()
#         # Don't know what I'm doing here, just testing
#         concerts_genre = Concert.query.filter(Concert.genre.like(search_query)).all()
#         #concerts = Concert.query.filter(Concert.city.like(search_query)).all()
#         return render_template('concerts/search.html', concerts=concerts, concerts_genre=concerts_genre)
#     else:
#         concerts=Concert.query.all()
#         return render_template('index.html', concerts=concerts)