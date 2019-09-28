import typesystem

from . import models as users_models


class UserWrite(typesystem.Schema):
    username = typesystem.String(max_length=50)


class UserRef(typesystem.Schema):
    id = typesystem.Integer()

    async def get_object(self) -> users_models.User:
        return await users_models.User.objects.get(id=self.id)


class User(UserRef):
    username = typesystem.String(max_length=50)
    auth_token = typesystem.String(max_length=200)
