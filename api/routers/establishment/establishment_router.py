#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from db_engine import establishments_crud as crud
from db_engine.database import SessionLocal, engine
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from fastapi import APIRouter, Depends, HTTPException
from schemas.base_schema import API_RESPONSE
#  IMPORTING SCHEMAS
from schemas.establishments_schemas import Establishments, Establishments_Name

establishment_router = APIRouter(
    prefix="/establishments",
    tags=["establishments"],
)


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@establishment_router.get('/get_all_establishments')
def get_all_establishments(db=Depends(db)):
    """
    Get all Stablishment's
    ---

    Returns a list of all stablisment's saved in db.

    """
    data = crud.get_all_establishments(db)
    API_RESPONSE['size'] = len(data)
    API_RESPONSE['data'] = data

    return(API_RESPONSE)


@establishment_router.get('/get_by_id/{id}')
def get_record_by_id(id:int, db=Depends(db)):
    data = crud.filter_record_by_id(db, id)

    if data is None:
        API_RESPONSE['data'] = 'NO SE ENCONTRO REGISTRO'
    else:
        API_RESPONSE['data'] = data
    return (API_RESPONSE)

@establishment_router.post('/save_establishment')
def save_establishment(estbl: Establishments, db=Depends(db)):
    """
    Save New Stablishment
    ---

    Save a new 'full establishemt record'.

    """
    API_RESPONSE['data'] = crud.save_establishment(db, estbl)
    return (API_RESPONSE)


@establishment_router.post('/get_or_create_establishment')
def get_or_create_new_establishment(estb: Establishments_Name, db=Depends(db)):
    """
    Get or Create New Stablishment
    ---

    Gets or Create a new establishment based on argument passed with no exception. it will only look or create based on the argument.

    """
    API_RESPONSE['data'] = crud.get_or_create_establishment(db, estb)
    return (API_RESPONSE)


@establishment_router.get('/filter_by_name/{establishment_name}')
def establishment_by_name(establishment_name: str, db=Depends(db)):
    """
    Get Stablishment by Name
    ---

    Filters stablishments by name and returns a list of all ocurrences.

    """
    data = crud.filter_establishment_by_content(db, establishment_name)
    API_RESPONSE['size'] = len(data)
    API_RESPONSE['data'] = data
    return (API_RESPONSE)


@establishment_router.get('/filter_by_name/{establishment_name}/{cant}')
def establishment_by_name_cant(establishment_name: str,
                               cant: int,
                               db=Depends(db)):
    """
    Stablishment by Name and Cant
    ---


    Filters records by 'establishment name' and returns the first set of N records if they exists.

    """
    data = crud.filter_establishment_by_content_limit_cant(
        db, establishment_name, cant)
    API_RESPONSE['size_exprected'] = cant
    API_RESPONSE['size'] = len(data)
    API_RESPONSE['data'] = data
    return (API_RESPONSE)
