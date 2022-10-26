from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()
app=Flask(__name__)

#create a function that creates a web application
# a web server will run this web application
def create_app():

   app.debug=True
   app.secret_key='utroutoru'
   #set the app configuration data 
   app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///sitedata.sqlite'
   #initialize db with flask app
   db.init_app(app)

   bootstrap = Bootstrap5(app)
   
   #initialize the login manager
   login_manager = LoginManager()
   
   #set the name of the login function that lets user login
   # in our case it is auth.login (blueprintname.viewfunction name)
   login_manager.login_view='auth.login'
   login_manager.init_app(app)

   #create a user loader function takes userid and returns User
   from .models import User  # importing here to avoid circular references
   @login_manager.user_loader
   def load_user(user_id):
      return User.query.get(int(user_id))

   #importing views module here to avoid circular references
   # a commonly used practice.
   from . import views
   app.register_blueprint(views.bp)
   from . import concerts
   app.register_blueprint(concerts.bp)
   from . import auth
   app.register_blueprint(auth.bp)
   
   return app

@app.errorhandler(404) 
def not_found(e): 
   return render_template("404.html"), 404