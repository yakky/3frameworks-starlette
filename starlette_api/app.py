import uvicorn
from starlette.applications import Starlette
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.responses import PlainTextResponse
from starlette.routing import Mount

from users import UsersApp, auth
from warehouse import WarehouseApp

from . import settings
from .database import database

routes = [Mount("/users", app=UsersApp), Mount("/", app=WarehouseApp)]

app = Starlette(routes=routes)
app.debug = settings.DEBUG
app.add_middleware(
    AuthenticationMiddleware,
    backend=auth.ModelTokenAuth(),
    on_error=lambda _, exc: PlainTextResponse(str(exc), status_code=401),
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ in ["__main__", "app"]:
    uvicorn.run(app, host="0.0.0.0", port=8000)
