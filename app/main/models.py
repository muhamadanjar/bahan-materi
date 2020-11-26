from app.models import ModelBase
from app import db


class Photos(ModelBase):
    __tablename__ = 'photos'
    id = db.Column(db.Integer, primary_key=True)
    lon =  db.Column(db.Float)
    lat =  db.Column(db.Float)
    nama = db.Column(db.Text)
    remark = db.Column(db.Text)
    uploader = db.Column(db.Text)
    ugroup = db.Column(db.Text)
    photo = db.Column(db.Text)

