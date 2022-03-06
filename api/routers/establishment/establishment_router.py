#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from fastapi import Depends, HTTPException, APIRouter
from db_engine.database import SessionLocal, engine
from db_engine import establishments_crud as crud

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
    return crud.get_all_establishments(db)


@establishment_router.post('/save_establishment')
def save_establishment(estbl: Establishments, db=Depends(db)):
    return crud.save_establishment(db, estbl)


@establishment_router.post('/get_or_create_vaccine')
def get_or_create_new_establishment(estb: Establishments_Name, db=Depends(db)):
    return crud.get_or_create_establishment(db, estb)
