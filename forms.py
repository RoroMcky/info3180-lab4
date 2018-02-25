from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired 
from flask_wtf.file import FileField
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
     upload = FileField('image', validators=[FileRequired(),FileAllowed(['jpg', 'png','jpeg'])])

    
    