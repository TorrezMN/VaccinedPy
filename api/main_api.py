from fastapi import FastAPI, Depends, HTTPException
from db_engine.database import SessionLocal, engine
from sqlalchemy.orm import Session
from db_engine.schema import Establishments, Dose, Record
from db_engine import crud, models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get('/')
def api_home():
    return ({
        'hell0': 'world',
    })


@app.post('/save_establishment')
def save_establishment(estbl: Establishments, db=Depends(db)):
    return crud.save_establishment(db, estbl)


@app.get('/get_all_establishments')
def get_all_establishments(db=Depends(db)):
    return crud.get_all_establishments(db)


@app.post('/save_dose')
def save_dose(dose: Dose, db=Depends(db)):
    return crud.save_dose(db, dose)


@app.get('/get_all_dose')
def get_all_dose(db=Depends(db)):
    return crud.get_all_dose(db)


@app.post('/add_new_record')
def add_new_record(rec: Record, db=Depends(db)):
    return crud.save_new_record(db, rec)
