from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from databases import Database
from app.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
database = Database(SQLALCHEMY_DATABASE_URL)
