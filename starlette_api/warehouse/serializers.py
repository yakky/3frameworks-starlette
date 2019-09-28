import typesystem

from starlette_api.users import serializers as users_serializers

from . import models as warehouse_models


class Organization(typesystem.Schema):
    id = typesystem.Integer(allow_null=True)
    name = typesystem.String(max_length=50, allow_blank=True)
    user = typesystem.Reference(users_serializers.UserRef, allow_null=True)

    async def get_object(self) -> warehouse_models.Organization:
        return await warehouse_models.Organization.objects.get(id=self.id)


class OrganizationCreate(Organization):
    user = typesystem.Reference(users_serializers.UserRef)


class Shelf(typesystem.Schema):
    id = typesystem.Integer(allow_null=True)
    organization = typesystem.Reference(Organization, allow_null=True)
    size = typesystem.Integer(allow_null=True)

    async def get_object(self) -> warehouse_models.Shelf:
        return await warehouse_models.Shelf.objects.get(id=self.id)


class ShelfCreate(Shelf):
    organization = typesystem.Reference(Organization)


class Box(typesystem.Schema):
    id = typesystem.Integer(allow_null=True)
    shelf = typesystem.Reference(Shelf, allow_null=True)

    async def get_object(self) -> warehouse_models.Box:
        return await warehouse_models.Box.objects.get(id=self.id)


class BoxCreate(Box):
    shelf = typesystem.Reference(Shelf, allow_null=True)
