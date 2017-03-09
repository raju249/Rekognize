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


engine = create_engine("sqlite:///mapping.db")
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)