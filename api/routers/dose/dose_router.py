#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from fastapi import Depends, HTTPException, APIRouter
from db_engine.schema import Dose
from db_engine.database import SessionLocal, engine
from db_engine import crud

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
    return crud.get_all_dose(db)


@dose_router.post('/save_dose')
def save_dose(dose: Dose, db=Depends(db)):
    return crud.save_dose(db, dose)
