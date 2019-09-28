import sqlalchemy

from starlette_api.database import database, metadata
from starlette_api.users.models import User  # NOQA
from starlette_api.warehouse.models import Box, Organization, Shelf  # NOQA

engine = sqlalchemy.create_engine(str(database.url))
metadata.drop_all(engine)
metadata.create_all(engine)
