import orm

from starlette_api.database import database, metadata
from starlette_api.users import models as users_models


class Organization(orm.Model):
    __tablename__ = "organization"
    __metadata__ = metadata
    __database__ = database

    id = orm.Integer(primary_key=True)
    name = orm.String(max_length=50)
    user = orm.ForeignKey(users_models.User)

    @classmethod
    async def get_or_create(cls, data: dict, **kwargs) -> "Organization":
        try:
            return await cls.objects.get(id=data["id"])
        except:
            return await cls.objects.create(**data)


class Shelf(orm.Model):
    __tablename__ = "shelf"
    __metadata__ = metadata
    __database__ = database
    id = orm.Integer(primary_key=True)
    organization = orm.ForeignKey(Organization)
    size = orm.Integer()

    @classmethod
    async def get_or_create(cls, data: dict, **kwargs) -> "Shelf":
        try:
            return await cls.objects.get(id=data["id"])
        except:
            return await cls.objects.create(**data)


class Box(orm.Model):
    __tablename__ = "box"
    __metadata__ = metadata
    __database__ = database
    id = orm.Integer(primary_key=True)
    shelf = orm.ForeignKey(Shelf)

    @classmethod
    async def get_or_create(cls, data: dict, **kwargs) -> "Box":
        try:
            return await cls.objects.get(id=data["id"])
        except:
            return await cls.objects.create(**data)
