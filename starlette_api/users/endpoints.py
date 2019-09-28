from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse

from . import models as users_models, serializers as users_serializers


class Users(HTTPEndpoint):
    async def get(self, request: Request) -> JSONResponse:
        users = await users_models.User.objects.all()
        return JSONResponse([dict(users_serializers.User(user)) for user in users])

    async def post(self, request: Request) -> JSONResponse:
        data = await request.json()
        user_data, errors = users_serializers.UserWrite.validate_or_error(data)
        if errors:
            return JSONResponse(dict(errors), status_code=400)
        user = await users_models.User.objects.create(**user_data)
        return JSONResponse(dict(users_serializers.User(user)))
