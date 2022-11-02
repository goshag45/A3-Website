from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for
from .models import Concert, Comment
from .forms import ConcertForm, CommentForm
from flask_login import login_required, current_user
from . import db
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
import os

bp = Blueprint('concert', __name__, url_prefix='/concerts')

@bp.route('/<id>')
def show(id):
    concert = Concert.query.filter_by(id=id).first()
    # create the comment form
    cform = CommentForm() 
    return render_template('concerts/show.html', concert=concert)

@bp.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
  print('Method type: ', request.method)
  form = ConcertForm()
  print('CREATE IS CALLED')
  if form.validate_on_submit():
    print('FORM IS VALID')
    #call the function that checks and returns image
    db_file_path=check_upload_file(form)
    concert=Concert(
    name=form.name.data,
    description=form.description.data, 
    genre=form.genre.data,
    image=db_file_path,
    datetime=form.datetime.data,
    address=form.address.data,
    city=form.city.data 
    )
    # add the object to the db session
    db.session.add(concert)
    # commit to the database
    db.session.commit()
    print('Successfully created new concert', 'success')
    #Always end with redirect when form is valid
    return redirect(url_for('concert.create'))
  return render_template('concerts/create.html', form=form)

def check_upload_file(form):
  #get file data from form  
  fp=form.image.data
  filename=fp.filename
  #get the current path of the module file… store image file relative to this path  
  BASE_PATH=os.path.dirname(__file__)
  #upload file location – directory of this file/static/image
  upload_path=os.path.join(BASE_PATH,secure_filename(filename))
  #store relative path in DB as image location in HTML is relative
  db_upload_path=secure_filename(filename)
  #save the file and return the db upload path  
  fp.save(upload_path)
  return db_upload_path

@bp.route('/<concert>/comment', methods = ['GET', 'POST'])  
@login_required
def comment(concert):  
    form = CommentForm()  
    concert_obj = Concert.query.filter_by(id=concert).first()  
    if form.validate_on_submit():  
      #read the comment from the form
      comment = Comment(text=form.text.data,  
                        destination=concert_obj,
                        user=current_user) 
      db.session.add(comment) 
      db.session.commit() 
      #flashing a message which needs to be handled by the html
      #flash('Your comment has been added', 'success')  
      print('Your comment has been added', 'success') 
    return redirect(url_for('concert.show', id=concert))
    