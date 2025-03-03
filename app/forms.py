from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Email


class ContactForm(FlaskForm):
    name = StringField('', validators=[InputRequired()])
    email = StringField('', validators=[InputRequired(), Email()])
    subject = StringField('', validators=[InputRequired()])
    message = TextAreaField('', validators=[InputRequired()])