import uvicorn

from typing import Union, List

from fastapi import FastAPI, Depends, HTTPException

from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# Dependency

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/addworkout/", response_model=schemas.Workout)
def create_workout(workout: schemas.WorkoutBase, db: Session = Depends(get_db)):
    return crud.create_workout(db=db, workout=workout)

@app.get("/allworkouts/", response_model=List[schemas.Workout])
def read_workouts(db: Session = Depends(get_db)):
    return crud.get_workouts(db)

@app.post('/filterworkouts/', response_model=List[schemas.Workout])
def filter_workouts(level:str, solo:bool, target_areas: schemas.TargetAreasFilter, ball:bool = False,  db: Session = Depends(get_db)):
    # print(target_areas, level)
    # print("hi")
    return crud.get_workouts_by_filters(db=db,level=level,ball=ball,solo=solo, target_areas=target_areas.target_areas)


# @app.get("/")
# def read_root():
#     return {" ": "World"}
#
# @app.get("/testing")
# def testing():
#     return {"Hello": "testing"}

# starts a server
if __name__ =="__main__":
    uvicorn.run("main:app",host='0.0.0.0', port=8889, reload=True)