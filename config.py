from sqlalchemy import MetaData, create_engine
from starlette.config import Config
from sqlalchemy.orm import declarative_base, sessionmaker


config = Config('.env')

# DATABASE
DATABASE_URL = config('DATABASE_URL')
engine = create_engine(DATABASE_URL)
Session = sessionmaker(engine)
session = Session()

DEBUG = config('DEBUG', cast=bool, default=False)


# SQLAlchemy
metadata = MetaData(engine)
Base = declarative_base()
