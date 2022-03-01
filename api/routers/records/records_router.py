#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from fastapi import Depends, HTTPException, APIRouter
from db_engine.schema import Record
from db_engine.database import SessionLocal, engine
from db_engine import crud

record_router = APIRouter(
    prefix="/record",
    tags=["record"],
)


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@record_router.post('/add_new_record')
def add_new_record(rec: Record, db=Depends(db)):
    return crud.save_new_record(db, rec)