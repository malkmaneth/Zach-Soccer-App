from sqlalchemy.orm import Session

import models, schemas

def create_workout(db: Session, workout: schemas.WorkoutBase):
    db_workout = models.Workout(**workout.dict())
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout

def get_workouts_by_filters(db: Session, level:str, ball:bool, solo:bool, target_areas: list):
    return db.query(models.Workout). \
        filter(models.Workout.level == level, models.Workout.ball == ball, models.Workout.solo == solo).\
        filter(*[models.Workout.target_areas.like(f"%{ta}%") for ta in target_areas]).all()

def get_workouts(db: Session):
    return db.query(models.Workout).all()