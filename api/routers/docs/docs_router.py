#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from fastapi import Depends, HTTPException, APIRouter
from db_engine.database import SessionLocal, engine
from db_engine import crud

#  IMPORTING SCHEMAS

docs_router = APIRouter(
    prefix="/docs",
    include_in_schema=False,
    tags=["docs"],
)


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@docs_router.get('/')
def docs_home(db=Depends(db)):
    return ({
        'docs': 'home',
    })


@docs_router.get('/dose')
def docs_dose(db=Depends(db)):
    return ({
        'dose': 'home',
    })


@docs_router.get('/establishments')
def docs_dose(db=Depends(db)):
    return ({
        'establishments': 'home',
    })


@docs_router.get('/vaccine')
def docs_dose(db=Depends(db)):
    return ({
        'vaccine': 'home',
    })


@docs_router.get('/records')
def docs_dose(db=Depends(db)):
    return ({
        'records': 'home',
    })
