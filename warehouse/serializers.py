from marshmallow import Schema, fields, post_load

from users import serializers as auth_serializers

from . import models as warehouse_models


class Organization(Schema):
    user = fields.Nested(auth_serializers.User)

    class Meta:
        fields = ("id", "name", "user")

    @post_load
    def get(self, data, **kwargs):
        return warehouse_models.Organization(**data)


class Shelf(Schema):
    organization = fields.Nested(Organization)

    class Meta:
        fields = ("id", "organization", "size")

    @post_load
    def get(self, data, **kwargs):
        return warehouse_models.Shelf(**data)


class Box(Schema):
    shelf = fields.Nested(Shelf)

    class Meta:
        fields = ("id", "shelf")

    @post_load
    def get(self, data, **kwargs):
        return warehouse_models.Box(**data)
