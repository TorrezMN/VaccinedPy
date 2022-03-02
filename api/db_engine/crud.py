#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN
#  FILTRAR POR CONTENIDO
#  Model.query.filter(Model.columnName.contains('sub_string'))

from db_engine import models
from sqlalchemy.orm import Session
#  IMPORTING SCHEMAS
from schemas.establishments_schemas import Establishments
from schemas.dose_schemas import Dose
from schemas.vaccine_schemas import Vaccine
from schemas.record_chemas import Record


def save_establishment(db: Session, info: Establishments):
    est = models.Establishments(**info.dict())
    db.add(est)
    db.commit()
    db.refresh(est)
    return (est)


def get_all_establishments(db: Session):
    return db.query(models.Establishments).all()


def save_dose(db: Session, info: Dose):
    dose = models.Dose(**info.dict())
    db.add(dose)
    db.commit()
    db.refresh(dose)
    return (dose)


def get_all_dose(db: Session):
    return db.query(models.Dose).all()


def save_new_vaccine(db: Session, vacc: Vaccine):
    v = models.Vaccine(**vacc.dict())
    db.add(v)
    db.commit()
    db.refresh(v)
    return (v)


def get_all_vaccines(db: Session):
    return db.query(models.Vaccine).all()


def save_new_record(db: Session, rec: Record):
    rec = models.Person_Record(**rec.dict())
    db.add(rec)
    db.commit()
    db.refresh(rec)
    return (rec)


def get_all_records(db: Session):
    return db.query(models.Person_Record).all()


def error_message(message):
    return {'error': message}
