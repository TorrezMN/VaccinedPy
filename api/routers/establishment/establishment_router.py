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
    Gets a full list of testablishments.
    """
    data = crud.get_all_establishments(db)
    API_RESPONSE['size'] = len(data)
    API_RESPONSE['data'] = data
    return (API_RESPONSE)


@establishment_router.post('/save_establishment')
def save_establishment(estbl: Establishments, db=Depends(db)):
    """
    Save a new 'full establishemt record'.

    ...

    Attributes
    ----------
    estbl : Establishments
        A data of type Establishemt to be saved.
    """
    API_RESPONSE['data'] = crud.save_establishment(db, estbl)
    return (API_RESPONSE)


@establishment_router.post('/get_or_create_establishment')
def get_or_create_new_establishment(estb: Establishments_Name, db=Depends(db)):
    """
    Gets or Create a new establishment based on argument passed with no exception. it will only look or create based on the argument.
    ...

    Attributes
    ----------
    eestablishment_name : str
        The name of the 'establishment' to be saved or created.
    """
    API_RESPONSE['data'] = crud.get_or_create_establishment(db, estb)
    return (API_RESPONSE)


@establishment_router.get('/filter_by_name/{establishment_name}')
def establishment_by_name(establishment_name: str, db=Depends(db)):
    """
    Filters stablishments by name and returns a list of all ocurrences.

    ...

    Attributes
    ----------
    establishment_name : str
        Establishment name to be used as filter parameter.
    """
    data = crud.filter_establishment_by_content(db, establishment_name)
    API_RESPONSE['size'] = len(data)
    API_RESPONSE['data'] = data
    return (API_RESPONSE)


@establishment_router.get('/filter_by_name/{establishment_name}/{cant}')
def establishment_by_name(establishment_name: str, cant: int, db=Depends(db)):
    """
    Filters records by 'establishment name' and returns the first set of N records if they exists.

    ...

    Attributes
    ----------
    establishment_name : str
        Establishment name to be used as filter parameter.

    cant : int
        Maximum number of records expected in response.
    """
    data = crud.filter_establishment_by_content_limit_cant(
        db, establishment_name, cant)
    API_RESPONSE['size_exprected'] = cant
    API_RESPONSE['size'] = len(data)
    API_RESPONSE['data'] = data
    return (API_RESPONSE)
