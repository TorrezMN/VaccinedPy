#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from fastapi import Depends, HTTPException, APIRouter
from db_engine.database import SessionLocal, engine
#  IMPORTING CRUDS
from db_engine import dose_crud, establishments_crud, vaccine_crud,records_crud

#  IMPORTING SCHEMAS
from schemas.base_schema import API_RESPONSE

miss_router = APIRouter(
    prefix="/miscellaneous",
    tags=["miscellaneous"],
)


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



@miss_router.get('/get_clean_record/{id}')
async def get_clean_record(id: int, db=Depends(db)):
    """
    Get Clean Record
    ---

    Returns a clean record to be shown in templates.

    """
    record = {}
    record_data = records_crud.filter_record_by_id(db, id)
    record["cedula"] = record_data.cedula
    record["fecha_aplicacion"] = record_data.fecha_aplicacion
    record["establishment"] = establishments_crud.filter_record_by_id(db, record_data.establishment).establishments_name
    record["vaccine"] = vaccine_crud.filter_record_by_id(db, record_data.vaccine).vaccine_name
    record["nombre"] = record_data.nombre
    record["apellido"] = record_data.apellido
    record["actualizado_al"] = record_data.actualizado_al
    record['dose'] = dose_crud.filter_record_by_id(db, record_data.dose).dose_number


    API_RESPONSE['data'] = record
    return (API_RESPONSE)

