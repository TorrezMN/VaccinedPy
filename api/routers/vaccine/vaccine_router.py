#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from fastapi import Depends, HTTPException, APIRouter
from db_engine.database import SessionLocal, engine
from db_engine import crud

#  IMPORTING SCHEMAS
from schemas.vaccine_schemas import Vaccine

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
def get_all_dose(db=Depends(db)):
    return crud.get_all_vaccines(db)


@vaccine_router.post('/add_new_vaccine')
def add_new_vaccine(vacc: Vaccine, db=Depends(db)):
    return crud.save_new_vaccine(db, vacc)
