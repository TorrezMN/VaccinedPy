#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN
from db_engine import models
#  IMPORTING SCHEMAS
from schemas.vaccine_schemas import Vaccine, Vaccine_Name
from sqlalchemy.orm import Session


def save_new_vaccine(db: Session, vacc: Vaccine):
    v = models.Vaccine(**vacc.dict())
    db.add(v)
    db.commit()
    db.refresh(v)
    return (v)


def get_all_vaccines(db: Session):
    return db.query(models.Vaccine).all()


def get_or_create_vaccine(db: Session, vacc: Vaccine_Name):
    instance = db.query(models.Vaccine).filter_by(**vacc.dict()).first()
    if instance:
        return instance
    else:
        v = models.Vaccine(**vacc.dict())
        db.add(v)
        db.commit()
        db.refresh(v)
        return (v)


def get_vaccine_by_name(db: Session, vacc: Vaccine_Name):
    instance = db.query(models.Vaccine).filter(
        models.Vaccine.vaccine_name.like(vacc)).first()

    if instance:
        return (instance)
    else:
        return ('Vaccine not found.!')
