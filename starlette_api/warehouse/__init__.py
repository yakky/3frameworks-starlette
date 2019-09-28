from starlette.routing import Route, Router

from . import endpoints

WarehouseApp = Router(
    [
        Route("/organizations/", endpoint=endpoints.Organizations, methods=["GET", "POST"]),
        Route("/shelves/", endpoint=endpoints.Shelves, methods=["GET", "POST"]),
        Route("/boxes/", endpoint=endpoints.Boxes, methods=["GET", "POST"]),
    ]
)
