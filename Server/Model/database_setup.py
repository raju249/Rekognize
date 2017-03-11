# We use the SQLAlchey object relational mapper for ORM.
# Below are the libs that we normally import to setup using the database using SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base  = declarative_base()

class Mapping(Base):
	__tablename__ = 'mapping'

	id = Column(Integer, primary_key = True)
	name = Column(String(250), unique = False, nullable = False)
	face_id = Column(String(1000), unique = True, nullable = False)


# Pass the database file path here.
engine = create_engine("sqlite:///D:\\Rekognize\\mapping.db")
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)