from fastapi import FastAPI, Depends, HTTPException
from db_engine.database import SessionLocal, engine
from sqlalchemy.orm import Session
from db_engine.schema import Establishments, Dose, Record
from db_engine import crud, models

#  IMPORTING ROUTERS
from routers.dose import dose_router
from routers.establishment import establishment_router
from routers.records import records_router
from routers.vaccine import vaccine_router

models.Base.metadata.create_all(bind=engine)

#  IMPORTING METADATA
from api_metadata import api_metadata

app = FastAPI(title="ESTE TITULO",
              description="UNA DESCRIPCION MUY LINDA.",
              version="0.0.1",
              openapi_tags=api_metadata)

#  INCLUDING ROUTERS
app.include_router(dose_router.dose_router, tags=['items'])
app.include_router(establishment_router.establishment_router)
app.include_router(vaccine_router.vaccine_router)
app.include_router(records_router.record_router)


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
