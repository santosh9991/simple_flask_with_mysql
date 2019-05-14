
from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root: @127.0.0.1:3306/tamuk', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()
class UserModel(Base):
    __tablename__ = 'users'
    kid = Column(Integer,primary_key=True)
    first_name = Column(Unicode)
    last_name = Column(Unicode)
    pwd = Column(Unicode)
    