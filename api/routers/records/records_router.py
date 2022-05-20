#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from db_engine import records_crud as crud
from db_engine.database import SessionLocal, engine
from fastapi import APIRouter, Depends, HTTPException
from schemas.base_schema import API_RESPONSE
#  IMPORTING SCHEMAS
from schemas.record_chemas import Record

record_router = APIRouter(
    prefix="/record",
    tags=["records"],
)


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@record_router.get('/get_all_records')
def all_records(db=Depends(db)):
    """
    USE WITH CAUTION - TAKES A LOT OF TIME
    ---

    Returns a full list of current records in the database.
    """
    return crud.get_all_records(db)


@record_router.post('/add_new_record')
def add_new_record(rec: Record, db=Depends(db)):
    """
    Add New Record
    ---

    Adds a 'complete' new record to the database.

    """
    return crud.save_new_record(db, rec)


@record_router.get('/filter_by_name/{name}')
def fileter_by_name(name: str, db=Depends(db)):
    """
    Filter by Name
    ---

    Filters records by name. RETURNS THE FIRST OCURRENCE.

    """
    data = crud.filter_record_by_name(db, name)
    API_RESPONSE['data'] = data
    return (API_RESPONSE)


@record_router.get('/filter_by_name_all/{name}')
def fileter_by_name_all(name: str, db=Depends(db)):
    """
    Filter by Name
    ---

    Filter all records by name and return all records that contain the name.

    """
    data = crud.filter_record_by_name_all(db, name)
    API_RESPONSE['data_size'] = len(data)
    API_RESPONSE['data'] = data
    return (API_RESPONSE)


@record_router.get('/filter_by_last_name/{last_name}')
def fileter_by_last_name(last_name: str, db=Depends(db)):
    """
    Filter by Last Name
    ---

    Filters all records by 'last name' and returns the first ocurrence.

    """
    data = crud.filter_record_by_last_name(db, last_name)
    API_RESPONSE['data'] = data
    return (API_RESPONSE)


@record_router.get('/filter_by_last_name_all/{last_name}')
def fileter_by_last_name_all(last_name: str, db=Depends(db)):
    """
    Filter by Last Name All
    ---

    Filter all recors by 'last name' and returns a full list of them.

    """
    data = crud.filter_record_by_last_name_all(db, last_name)
    API_RESPONSE['size'] = len(data)
    API_RESPONSE['data'] = data
    return (API_RESPONSE)


@record_router.get('/filter_by_ci/{ci}')
def fileter_by_ci(ci: str, db=Depends(db)):
    """
    Filter by CI
    ---

    Filters records by CI and returns the first ocurrence.

    """
    data = crud.filter_record_by_ci(db, ci)
    if data is None:
        API_RESPONSE['data'] = 'NO SE ENCONTRO REGISTRO'
    else:
        API_RESPONSE['data'] = data
    return (API_RESPONSE)


@record_router.get('/filter_if_contains_ci/{ci}')
def fileter_if_contains_ci(ci: str, db=Depends(db)):
    """
    Filter if Contains the N° given.
    ---

    Filters records by ci if record contains the numbers given and returns a list of records.

    """

    data = crud.filter_record_if_contains_ci(db, ci)
    if data is None:
        API_RESPONSE['data'] = 'NO SE ENCONTRO REGISTRO'
    else:
        API_RESPONSE['size'] = len(data)
        API_RESPONSE['data'] = data
    return (API_RESPONSE)


#  REGISTRO
#  ==========================
#  'nombre'
#  'apellido'
#  'establecimiento'
#  'fecha_aplicacion'
#  'cedula'
#  'dosis'
#  'descripcion_vacuna'
#  'actualizado_al'
@record_router.get('/filter_by_application_date_all/{date}')
def filter_by_application_date_all(date: str, db=Depends(db)):
    """
    Filter by Application Date
    ---

    Filters all records in wich 'fecha_aplicacion' matchs the requested date.

    """
    data = crud.filter_record_by_application_date(db, date)
    API_RESPONSE['size'] = len(data)
    API_RESPONSE['data'] = data
    return (data)


@record_router.get('/filter_by_application_date_limit/{date}/{cant}')
def filter_by_application_date_restricted_size(date: str,
                                               cant: int,
                                               db=Depends(db)):
    """
    Filter by Application Date and Cant
    ---

    Filters all records in wich 'fecha_aplicacion' matchs the requested date and returns the first N mathes.

    """
    data = crud.filter_record_by_application_date_restricted(db, date, cant)
    API_RESPONSE['requested_size'] = len(data)
    API_RESPONSE['size'] = len(data)
    API_RESPONSE['data'] = data
    return (API_RESPONSE)


