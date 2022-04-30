#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN


from pydantic import BaseModel
from sqlalchemy.orm import Session

#  {
  #  "nombre": "string",
  #  "apellido": "string",
  #  "fecha_aplicacion": "2022-04-29",
  #  "cedula": "string",
  #  "establishment": 0,
  #  "dose": 0,
  #  "vaccine": 0,
  #  "actualizado_al": "2022-04-29"
#  }

class Vaccine_Name(BaseModel):
    vaccine_name : str
    class Config:
        orm_mode = True

class Establishments_Name(BaseModel):
    establishments_name : str
    class Config:
        orm_mode = True

class Dose_Name(BaseModel):
    dose_number : int 
    class Config:
        orm_mode = True

class Record(BaseModel):
    nombre : str 
    apellido : str 
    fecha_aplicacion : date 
    cedula : str 
    establishment : int 
    dose : int 
    vaccine : int 
    actualizado_al: date 

    class Config:
        orm_mode = True


def save_new_record(db: Session, rec: Record):
    rec = models.Person_Record(**rec.dict())
    db.add(rec)
    db.commit()
    db.refresh(rec)
    return (rec)

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
