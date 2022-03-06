#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN
from db_engine import models
from schemas.dose_schemas import Dose
#  IMPORTING SCHEMAS
from schemas.establishments_schemas import Establishments, Establishments_Name
from schemas.record_chemas import Record
from schemas.vaccine_schemas import Vaccine
from sqlalchemy.orm import Session

#  def get_or_create(db:Session, model, **kwargs):
#  instance = session.query(model).filter_by(**kwargs).first()
#  if instance:
#  return instance
#  else:
#  instance = model(**kwargs)
#  session.add(instance)
#  session.commit()
#  return instance


def save_new_record(db: Session, rec: Record):
    rec = models.Person_Record(**rec.dict())
    db.add(rec)
    db.commit()
    db.refresh(rec)
    return (rec)


def get_all_records(db: Session):
    return db.query(models.Person_Record).all()
