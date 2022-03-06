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


def get_all_establishments(db: Session):
    return db.query(models.Establishments).all()


def filter_establishment_name(db: Session, estb_name: Establishments_Name):
    return db.query(models.Establishments).filter(
        models.Establishments.establishments_name.contains(estb_name)).first()


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
