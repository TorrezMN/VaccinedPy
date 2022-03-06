#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from fastapi import Depends, HTTPException, APIRouter
from db_engine.database import SessionLocal, engine
from db_engine import records_crud as crud

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
def add_new_record(db=Depends(db)):
    return crud.get_all_records(db)


@record_router.post('/add_new_record')
def add_new_record(rec: Record, db=Depends(db)):
    return crud.save_new_record(db, rec)
