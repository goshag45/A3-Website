from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Concert
from .forms import ConcertForm

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    form = ConcertForm()
    concerts=Concert.query.all()
    return render_template('index.html', form=form, concerts=concerts)


@bp.route('/search')
def search():
    form=ConcertForm()
    if request.args['search']:
        print(request.args['search'])
        print("I AM HERE HELLOOOOOOO")
        search_query = "%" + request.args['search'] + '%'
        concerts = Concert.query.filter(Concert.name.like(search_query)).all()
        # Don't know what I'm doing here, just testing
        #if request.option != 'select a genre':
         #   concerts_genre = Concert.query.filter(Concert.genre.data.like(search_query)).all()
        #else:
         #   print("it is not working. sorry")
        #concerts = Concert.query.filter(Concert.city.like(search_query)).all()
        #return render_template('concerts/search.html', concerts=concerts, concerts_genre=concerts_genre)
        return render_template('concerts/search.html', concerts=concerts)
    elif request.args.get("genre_options"):
        # Look into the database for all results
        print("bbb")
        searches = Concert.query.all()
        search_query = request.args.get("genre_options")
        concerts = Concert.query.filter(Concert.genre.like(search_query)).all()
        print(search_query)
        # Search the user input in all results
        for search in searches:
            # if there is anything matches with the user input, return it as results
            if search == search_query:
                
                return render_template('concerts/search.html')
            else:
                print("i dont know what to do")
            
        return render_template('concerts/search.html', concerts=concerts)
    else:
        print("aaa")
        concerts=Concert.query.all()
        return render_template('index.html', form=form, concerts=concerts)

        
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