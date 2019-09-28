from marshmallow import Schema, fields, post_load

from . import models as auth_models


class User(Schema):
    id = fields.Integer()
    auth_token = fields.String(max_length=200, dump_only=True)

    class Meta:
        fields = ("username", "auth_token", "id")

    @post_load
    def get(self, data, **kwargs):
        return auth_models.User(**data)
