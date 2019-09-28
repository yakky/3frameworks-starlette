import databases
import sqlalchemy

from . import settings

database = databases.Database(settings.DATABASE_URL)
metadata = sqlalchemy.MetaData()
