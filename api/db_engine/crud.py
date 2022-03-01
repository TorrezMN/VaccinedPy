#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from db_engine import models, schema
from sqlalchemy.orm import Session


def save_establishment(db: Session, info: schema.Establishments):
    est = models.Establishments(**info.dict())
    db.add(est)
    db.commit()
    db.refresh(est)
    return (est)


def get_all_establishments(db: Session):
    return db.query(models.Establishments).all()


def save_dose(db: Session, info: schema.Dose):
    dose = models.Dose(**info.dict())
    db.add(dose)
    db.commit()
    db.refresh(dose)
    return (dose)


def get_all_dose(db: Session):
    return db.query(models.Dose).all()


def save_new_vaccine(db: Session, vacc: schema.Vaccine):
    v = models.Vaccine(**vacc.dict())
    db.add(v)
    db.commit()
    db.refresh(v)
    return (v)


def save_new_record(db: Session, rec: schema.Record):
    rec = models.Person_Record(**rec.dict())
    db.add(rec)
    db.commit()
    db.refresh(rec)
    return (rec)


def error_message(message):
    return {'error': message}
