from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base
# imports the base variable from the database.py file

class Workout(Base):
    __tablename__ = "workout"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    target_areas = Column(String, index=True)
    level = Column(String, index=True)
    reps = Column(Integer, index=True)
    sets = Column(Integer, index=True)
    ball = Column(Boolean, default=False)
    solo = Column (Boolean, default=True)

# .dict() converts it to a dictionary that looks like this:
# {"id":2, "name":"dsglkjg"}