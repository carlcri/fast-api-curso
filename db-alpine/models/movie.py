from sqlalchemy import Column, Integer, String, Float
from config.database import Base

class Movie(Base):

    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)