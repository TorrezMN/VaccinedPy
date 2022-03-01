#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from fastapi import Depends, HTTPException, APIRouter
from db_engine.schema import Establishments
from db_engine.database import SessionLocal, engine
from db_engine import crud

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


@establishment_router.post('/save_establishment')
def save_establishment(estbl: Establishments, db=Depends(db)):
    return crud.save_establishment(db, estbl)


@establishment_router.get('/get_all_establishments')
def get_all_establishments(db=Depends(db)):
    return crud.get_all_establishments(db)
