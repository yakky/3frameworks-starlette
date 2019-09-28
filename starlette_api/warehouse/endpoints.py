from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse

from . import models as warehouse_models, serializers as warehouse_serializers


class Organizations(HTTPEndpoint):
    async def get(self, request: Request) -> JSONResponse:
        organizations = await warehouse_models.Organization.objects.all()
        return JSONResponse([dict(warehouse_serializers.Organization(organization)) for organization in organizations])

    async def post(self, request: Request) -> JSONResponse:
        data = await request.json()
        organization_data, errors = warehouse_serializers.OrganizationCreate.validate_or_error(data)
        if errors:
            return JSONResponse(dict(errors), status_code=400)
        data["user"] = await organization_data.user.get_object()
        organization = await warehouse_models.Organization.objects.create(**data)
        return JSONResponse(dict(warehouse_serializers.Organization(organization)))


class Shelves(HTTPEndpoint):
    async def get(self, request: Request) -> JSONResponse:
        shelves = await warehouse_models.Shelf.objects.all()
        return JSONResponse([dict(warehouse_serializers.Shelf(shelf)) for shelf in shelves])

    async def post(self, request: Request) -> JSONResponse:
        data = await request.json()
        shelf_data, errors = warehouse_serializers.ShelfCreate.validate_or_error(data)
        if errors:
            return JSONResponse(dict(errors), status_code=400)
        data["organization"] = await shelf_data.organization.get_object()
        shelf = await warehouse_models.Shelf.objects.create(**data)
        return JSONResponse(dict(warehouse_serializers.Shelf(shelf)))


class Boxes(HTTPEndpoint):
    async def get(self, request: Request) -> JSONResponse:
        boxes = await warehouse_models.Box.objects.all()
        return JSONResponse([dict(warehouse_serializers.Box(box)) for box in boxes])

    async def post(self, request: Request) -> JSONResponse:
        data = await request.json()
        box_data, errors = warehouse_serializers.BoxCreate.validate_or_error(data)
        if errors:
            return JSONResponse(dict(errors), status_code=400)
        data["shelf"] = await box_data.shelf.get_object()
        box = await warehouse_models.Box.objects.create(**data)
        return JSONResponse(dict(warehouse_serializers.Box(box)))
