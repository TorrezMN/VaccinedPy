#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from db_engine import models
from sqlalchemy.orm import Session
#  IMPORTING SCHEMAS
from schemas.dose_schemas import Dose, Dose_Name


def save_dose(db: Session, info: Dose):
    dose = models.Dose(**info.dict())
    db.add(dose)
    db.commit()
    db.refresh(dose)
    return (dose)


def get_all_dose(db: Session):
    return db.query(models.Dose).all()


def get_or_create_new_dose(db: Session, d: Dose_Name):
    instance = db.query(models.Dose).filter_by(**d.dict()).first()
    if instance:
        return instance
    else:
        v = models.Dose(**d.dict())
        db.add(v)
        db.commit()
        db.refresh(v)
        return (v)
