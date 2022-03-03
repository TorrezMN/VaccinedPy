#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from fastapi import Depends, HTTPException, APIRouter
from db_engine.database import SessionLocal, engine
from db_engine import crud

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


@establishment_router.post('/filter/{estb_name}')
def filter_establishment(estb_name: str, db=Depends(db)):
    return crud.filter_establishment_name(db, estb_name)
