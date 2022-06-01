#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from db_engine import models
#  IMPORTING SCHEMAS
from schemas.establishments_schemas import Establishments, Establishments_Name
from sqlalchemy.orm import Session


def save_establishment(db: Session, info: Establishments):
    est = models.Establishments(**info.dict())
    db.add(est)
    db.commit()
    db.refresh(est)
    return (est)

def filter_record_by_id(db: Session, id: int):
    return db.query(
        models.Establishments).filter(models.Establishments.id == id).first()

def get_all_establishments(db: Session):
    return db.query(models.Establishments).all()


def filter_establishment_name(db: Session, estb_name: Establishments_Name):
    return db.query(models.Establishments).filter(
        models.Establishments.establishments_name.contains(estb_name)).first()


def filter_establishment_by_content(db: Session,
                                    estb_name: Establishments_Name):
    data = db.query(models.Establishments).filter(
        models.Establishments.establishments_name.contains(estb_name)).all()
    return ({
        'data': data,
    })


def filter_establishment_by_content_limit_cant(db: Session,
                                               estb_name: Establishments_Name,
                                               cant: int):
    data = db.query(models.Establishments).filter(
        models.Establishments.establishments_name.contains(estb_name)).limit(
            cant).all()
    return (data)


def get_or_create_establishment(db: Session, estb: Establishments_Name):
    instance = db.query(models.Establishments).filter_by(**estb.dict()).first()
    if instance:
        return instance
    else:
        v = models.Establishments(**estb.dict())
        db.add(v)
        db.commit()
        db.refresh(v)
        return (v)
