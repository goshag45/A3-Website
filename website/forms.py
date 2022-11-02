from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, IntegerField, DateTimeLocalField , SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo, NumberRange
from flask_wtf.file import FileRequired, FileField, FileAllowed 

ALLOWED_FILE = {'PNG', 'JPG', 'png', 'jpg'}

#Create new concert
class ConcertForm(FlaskForm):
  name = StringField('Artist Name', validators=[InputRequired()])
  description = TextAreaField('Description', 
            validators=[InputRequired()])
  genreChoices = "Pop", "Country", "Jazz", "RnB", "Rock"
  genre = SelectField(u'Field name', choices = genreChoices , validators = [InputRequired()])
  image = FileField('Destination Image', validators=[
    FileRequired(message='Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')])
  datetime = DateTimeLocalField('Date', format='%Y-%m-%dT%H:%M', validators=[InputRequired("Missing Date or Time")])
  address = StringField('Address', validators=[InputRequired()])
  cityChoices = "Brisbane", "Sydney", "Melbourne", "Adelaide", "Perth"
  city = SelectField(u'Field name', choices = cityChoices, validators = [InputRequired()])
  tickets = IntegerField('Tickets', validators = [
    NumberRange(min=1, max=100000),
    InputRequired()])
  submit = SubmitField("Create")

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
    phone = StringField('Phone', validators=[InputRequired()])
    address = StringField('Address', validators=[InputRequired()])
    #submit button
    submit = SubmitField("Register")

#User comment
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')