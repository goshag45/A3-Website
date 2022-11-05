from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Concert, Comment
from datetime import datetime
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
        cmtform = CommentForm() 
        return render_template('concerts/show.html', cmtform=cmtform, concert=concert, id=id)

@bp.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
    print('CREATE IS CALLED')
    print('Method type: ', request.method)
    form = ConcertForm()
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
        city=form.city.data,
        # tickets=form.tickets.data,
        status=form.status.data
        )
        # add the object to the db session
        db.session.add(concert)
        # commit to the database
        db.session.commit()
        flash('Successfully created new concert', 'success')
        print('Successfully created new concert', 'success')
        #Always end with redirect when form is valid
        return redirect(url_for('concert.create'))
    return render_template('concerts/create.html', form=form)

# Youtube tutorial for updating the database: https://www.youtube.com/watch?v=Wicjkn5_nIQ
@bp.route('/update/<id>', methods = ['GET', 'POST'])
@login_required
def update(id):
    form = ConcertForm()
    name_to_update = Concert.query.get_or_404(id)
    if request.method == "POST":
        name_to_update.name = request.form['name']
        name_to_update.genre = request.form['genre']
        name_to_update.datetime = datetime.strptime(request.form['datetime'], "%Y-%m-%dT%H:%M")
        name_to_update.address = request.form['address']
        name_to_update.city = request.form['city']
        name_to_update.description = request.form['description']
        name_to_update.status = request.form['status']
        # try to commit it straight away instead going into try- statement error raise and fail to update the data
        db.session.commit()
        flash("Update successful!")
        try:
            db.session.commit()
            flash("User Updated Successfully!")
            return render_template("concerts/update.html", 
                form=form,
                name_to_update=name_to_update, id=id)
        except:
            db.session.rollback()
            flash("Error!  Looks like there was a problem...try again!")
            return render_template("concerts/update.html", 
                form=form,
                name_to_update = name_to_update,
                id=id)
    else:
        return render_template("concerts/update.html", 
                form=form,
                name_to_update = name_to_update,
                id = id)
                
@bp.route('/delete/<id>', methods = ['GET', 'POST'])
@login_required
def delete(id):
        form = ConcertForm()
        to_be_delete = Concert.query.get_or_404(id)
        try:
            db.session.delete(to_be_delete)
            db.session.commit()
            flash("The event has been successfully deleted.")
            return redirect(url_for('main.index'))
        except:
            flash("Unsuccessfully delete action.")
            return redirect(url_for('main.index'))

def check_upload_file(form):
    #get file data from form  
    fp=form.image.data
    filename=fp.filename
    #get the current path of the module file… store image file relative to this path  
    BASE_PATH=os.path.dirname(__file__)
    #upload file location – directory of this file/static/image
    upload_path=os.path.join(BASE_PATH,'static/img',secure_filename(filename))
    #store relative path in DB as image location in HTML is relative
    db_upload_path='/static/img/' + secure_filename(filename)
    #save the file and return the db upload path  
    fp.save(upload_path)
    return db_upload_path

@bp.route('/<id>/comment', methods = ['POST'])  
@login_required
# changing comment(concert) to comment(id) for testing
def comment(id):  
    cmtform = CommentForm()  
    concert_obj = Concert.query.filter_by(id=id).first()  
    if cmtform.validate_on_submit():  
        #read the comment from the form
        print("We got a comment: " + cmtform.text.data)
        comment = Comment(text=cmtform.text.data,  
                        concert=concert_obj,
                        user=current_user) 
        db.session.add(comment) 
        db.session.commit() 
        #flashing a message which needs to be handled by the html
        flash('Your comment has been added', 'success')  
        print('Your comment has been added', 'success') 
    return redirect(url_for('concert.show', id=id))