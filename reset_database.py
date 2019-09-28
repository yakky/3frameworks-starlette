import sqlalchemy

from starlette_api.database import database, metadata
from users.models import User  # NOQA
from warehouse.models import Box, Organization, Shelf  # NOQA

engine = sqlalchemy.create_engine(str(database.url))
metadata.drop_all(engine)
metadata.create_all(engine)
