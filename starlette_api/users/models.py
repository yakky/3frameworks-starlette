import orm
from itsdangerous import BadSignature, JSONWebSignatureSerializer as Serializer

from starlette_api import settings
from starlette_api.database import database, metadata


class User(orm.Model):
    __tablename__ = "user"
    __metadata__ = metadata
    __database__ = database

    id = orm.Integer(primary_key=True)
    username = orm.String(max_length=50, unique=True)

    @property
    def auth_token(self) -> str:
        s = Serializer(str(settings.SECRET_KEY))
        return s.dumps({"id": self.id}).decode()

    @staticmethod
    async def verify_auth_token(token: str) -> "User":
        s = Serializer(str(settings.SECRET_KEY))
        try:
            data = s.loads(token)
        except BadSignature:
            return None  # invalid token
        user = await User.objects.get(id=data["id"])
        return user

    @classmethod
    async def get_or_create(cls, data: dict, **kwargs) -> "User":
        try:
            return await cls.objects.get(id=data["id"])
        except:
            return await cls.objects.create(**data)
