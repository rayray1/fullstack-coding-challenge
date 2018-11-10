from app import db
from uuid import uuid4


class TranslationQuery(db.Model):
    id = db.Column(db.String, default=lambda: str(uuid4().hex), primary_key=True)
    queried_data = db.Column(db.String(200), unique=False)
