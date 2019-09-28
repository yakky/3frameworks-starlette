from marshmallow import ValidationError
from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse

from . import models, serializers


class Organizations(HTTPEndpoint):
    async def get(self, request):
        organizations = await models.Organization.objects.all()
        return JSONResponse(serializers.Organization(many=True).dump(organizations))

    async def post(self, request):
        data = await request.json()
        try:
            organization_data = serializers.Organization().load(data)
        except ValidationError as err:
            return JSONResponse(err.messages, status_code=400)
        organization = await models.Organization.get_or_create(organization_data)
        return JSONResponse(serializers.Organization().dump(organization))


class Shelves(HTTPEndpoint):
    async def get(self, request):
        shelves = await models.Shelf.objects.all()
        return JSONResponse(serializers.Shelf(many=True).dump(shelves))

    async def post(self, request):
        data = await request.json()
        try:
            shelf_data = serializers.Shelf().load(data)
        except ValidationError as err:
            return JSONResponse(err.messages, status_code=400)
        shelf = await models.Shelf.get_or_create(shelf_data)
        return JSONResponse(serializers.Shelf().dump(shelf))


class Boxes(HTTPEndpoint):
    async def get(self, request):
        boxes = await models.Box.objects.all()
        return JSONResponse(serializers.Box(many=True).dump(boxes))

    async def post(self, request):
        data = await request.json()
        try:
            box_data = serializers.Box().load(data)
        except ValidationError as err:
            return JSONResponse(err.messages, status_code=400)
        box = await models.Box.get_or_create(box_data)
        return JSONResponse(serializers.Box().dump(box))
