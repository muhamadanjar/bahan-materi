from app import ma
from app.main.models import Photos
from app.tematik.models import GisJenisTanah, GisPoi


class PhotosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Photos


class JenisTanahSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GisJenisTanah


class PoiSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GisPoi
        