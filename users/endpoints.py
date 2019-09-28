from marshmallow import ValidationError
from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse

from . import models, serializers


class Users(HTTPEndpoint):
    async def get(self, request):
        users = await models.User.objects.all()
        return JSONResponse(serializers.User(many=True).dump(users))

    async def post(self, request):
        data = await request.json()
        try:
            user_data = serializers.User().load(data)
        except ValidationError as err:
            return JSONResponse(err.messages, status_code=400)
        except Exception as err:
            return JSONResponse(str(err), status_code=400)
        user = await models.User.get_or_create(user_data)
        return JSONResponse(serializers.User().dump(user))
