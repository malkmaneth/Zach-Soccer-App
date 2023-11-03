from typing import List, Union
from pydantic import BaseModel
# bool, int

class WorkoutBase(BaseModel):
    name: str
    target_areas: str
    level: str
    reps: int
    sets: int
    ball: bool
    solo: bool

class TargetAreasFilter(BaseModel):
    target_areas: List[str]


class Workout(WorkoutBase):
    id: int

    class Config:
        orm_mode = True

#crud = Create Read Update Delete