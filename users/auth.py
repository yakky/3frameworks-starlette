import typing

import orm
from starlette import authentication as auth
from starlette_auth_toolkit.base.backends import BaseTokenAuth

from . import models as auth_models

_User = orm.Model


class ModelTokenAuth(BaseTokenAuth):
    model = auth_models.User

    async def find_user(self, username: str) -> typing.Optional[_User]:
        try:
            return await self.model.objects.get(username=username)
        except orm.NoMatch:
            return None

    async def verify(self, token: str) -> typing.Optional[auth.BaseUser]:
        user = await self.model.verify_auth_token(token)
        if user:
            return user
        return None
