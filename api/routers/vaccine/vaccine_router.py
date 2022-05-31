#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from fastapi import Depends, HTTPException, APIRouter
from db_engine.database import SessionLocal, engine
from db_engine import vaccine_crud as crud

#  IMPORTING SCHEMAS
from schemas.vaccine_schemas import Vaccine, Vaccine_Name
from schemas.base_schema import API_RESPONSE

vaccine_router = APIRouter(
    prefix="/vaccine",
    tags=["vaccine"],
)


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@vaccine_router.get('/get_all_vaccines')
def get_all_vaccines(db=Depends(db)):
    """
        Get all vaccines.
        ---
        Returns a list of all vaccines registered.
    """
    data = crud.get_all_vaccines(db)
    size = len(data)
    API_RESPONSE['size'] = size
    API_RESPONSE['data'] = data
    return (API_RESPONSE)


@vaccine_router.post('/add_new_vaccine')
def add_new_vaccine(vacc: Vaccine, db=Depends(db)):
    """
        Add new vaccine.
        ---
        Allows users to add new vaccines.
    """
    API_RESPONSE['data'] = crud.save_new_vaccine(db, vacc)
    return (API_RESPONSE)


@vaccine_router.post('/get_or_create_vaccine')
def get_or_create_new_vaccine(vacc: Vaccine_Name, db=Depends(db)):
    """
        GET or CREATE new Vaccine
        ---
        Returns a vaccine record if exists or create a new record and return the record created.

    """
    API_RESPONSE['data'] = crud.get_or_create_vaccine(db, vacc)
    return (API_RESPONSE)


@vaccine_router.post('/get_vaccine_by_name/{vacc_name}')
def get_vaccine_by_name(v_name: str, db=Depends(db)):
    API_RESPONSE['data'] = crud.get_vaccine_by_name(db, v_name)
    return (API_RESPONSE)
