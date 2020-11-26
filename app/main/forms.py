from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired



class PhotoForm(FlaskForm):
    nama = StringField(label='Nama')
    lat = FloatField(label='Latitude', validators=[DataRequired()])
    lon = FloatField(label='Longitude', validators=[DataRequired()])
    photo = FileField(validators=[FileRequired()])

