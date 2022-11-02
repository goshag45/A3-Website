from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, DateField, TimeField, SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed 

ALLOWED_FILE = {'PNG', 'JPG', 'png', 'jpg'}

#Create new concert
class ConcertForm(FlaskForm):
  artist_name = StringField('Artist Name', validators=[InputRequired()])
  description = TextAreaField('Description', 
            validators=[InputRequired()])
  genreChoices = "Pop", "Country", "Jazz", "RnB", "Rock"
  genre = SelectField(u'Field name', choices = genreChoices , validators = [InputRequired()])
  image = FileField('Destination Image', validators=[
    FileRequired(message='Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')])
  date = DateField('Date', format="%Y-%m-%d", validators=[InputRequired("Missing Date Input")])
  time = TimeField('Time', format="%H:%M",  validators=[InputRequired("Missing Time Input")])
  address = StringField('Address', validators=[InputRequired()])
  cityChoices = "Brisbane", "Sydney", "Melbourne", "Adelaide", "Perth"
  city = SelectField(u'Field name', choices = cityChoices, validators = [InputRequired()])
  submit = SubmitField("Create Event")

#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    #submit button
    submit = SubmitField("Register")

#User comment
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')