from datetime import datetime
import hashlib

from flask import current_app, request, url_for
from app.exceptions import ValidationError
from app import db

from sqlalchemy import func
from sqlalchemy import String
from sqlalchemy.ext.declarative import declared_attr


class CaseInsensitiveString(String):
    class comparator_factory(String.Comparator):
        def operate(self, op, other):
            return op(func.lower(self.expr), func.lower(other))


class ModelBase(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now())

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
