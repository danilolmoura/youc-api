from flask_potion import fields, ModelResource
from flask_potion.routes import ItemRoute, Route
from flask_jwt import jwt_required, current_identity
from werkzeug.exceptions import Forbidden

from application import db
from application.models import User


class UserResource(ModelResource):
    class Meta:
        include_id = True
        model = User
        name = 'user'
        exclude_fields = ['created_at']

    class Schema:
        pass

def create_api(api):
    api.add_resource(UserResource)
