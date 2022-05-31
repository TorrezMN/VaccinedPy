#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from fastapi import Depends, HTTPException, APIRouter
from db_engine.database import SessionLocal, engine
from db_engine import dose_crud as crud

#  IMPORTING SCHEMAS
from schemas.dose_schemas import Dose, Dose_Name
from schemas.base_schema import API_RESPONSE

dose_router = APIRouter(
    prefix="/dose",
    tags=["dose"],
)


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@dose_router.get('/get_all_dose')
def get_all_dose(db=Depends(db)):
    """
    Get All Dose
    ---

    Returns a list of ``all`` dose registered in the sistem.

    """

    data = crud.get_all_dose(db)
    size = len(data)
    API_RESPONSE['size'] = size
    API_RESPONSE['data'] = data
    return (API_RESPONSE)


@dose_router.post('/save_dose')
def save_dose(dose: Dose, db=Depends(db)):
    """
    Save Dose
    ---

    Allows user to save a new dose in the db.

    """
    API_RESPONSE['data'] = crud.save_dose(db, dose)
    return (API_RESPONSE)


@dose_router.post('/get_or_create_dose')
def get_or_create_new_dose(d: Dose_Name, db=Depends(db)):
    """
    Get or Create - Dose
    ---

    Allows users to ``get or create`` a new dose in the db.

    """
    API_RESPONSE['data'] = crud.get_or_create_new_dose(db, d)
    return (API_RESPONSE)
