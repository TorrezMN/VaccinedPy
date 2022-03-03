from fastapi import FastAPI, Depends, Request, HTTPException
from db_engine.database import SessionLocal, engine
from sqlalchemy.orm import Session
from db_engine import crud, models
import os
from pathlib import Path

#  STATIC/TEMPLATES IMPORTS
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

#  IMPORTING SCHEMAS
from schemas.dose_schemas import Dose
from schemas.establishments_schemas import Establishments
from schemas.record_chemas import Record

#  IMPORTING ROUTERS
from routers.dose import dose_router
from routers.establishment import establishment_router
from routers.records import records_router
from routers.vaccine import vaccine_router

models.Base.metadata.create_all(bind=engine)

#  IMPORTING METADATA
from api_metadata import api_metadata

app = FastAPI(title="Paraguay - COVID",
              description="A small api to explore COVID data of Paraguay..",
              version="0.0.1",
              openapi_tags=api_metadata)

#  INCLUDING ROUTERS
app.include_router(dose_router.dose_router)
app.include_router(establishment_router.establishment_router)
app.include_router(vaccine_router.vaccine_router)
app.include_router(records_router.record_router)

#  STATIC & TEMPLATES
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = os.path.join(BASE_DIR, 'static')
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
app.mount('/static', StaticFiles(directory=STATIC_DIR), name="static")
#
templates = Jinja2Templates(directory=TEMPLATES_DIR)


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get('/')
def api_home(request: Request, db=Depends(db)):
    return templates.TemplateResponse("index.html", {
        "request": request,
    })


#
