from starlette.routing import Route, Router

from . import endpoints

UsersApp = Router([Route("/", endpoint=endpoints.Users, methods=["GET", "POST"])])
