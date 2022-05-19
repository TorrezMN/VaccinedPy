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


def save_new_record(db: Session, rec: Record):
    rec = models.Person_Record(**rec.dict())
    db.add(rec)
    db.commit()
    db.refresh(rec)
    return (rec)


def update_record(db: Session, ci: str, rec: Record):
    n = str(ci)
    r = db.query(
        models.Person_Record).filter(models.Person_Record.cedula == n).first()

    r.nombre = rec.nombre
    r.apellido = rec.apellido
    r.fecha_aplicacion = rec.fecha_aplicacion
    r.cedula = rec.cedula
    r.establishment = rec.establishment
    r.dose = rec.dose
    r.vaccine = rec.vaccine
    r.actualizado_al = rec.actualizado_al

    db.add(r)
    db.commit()
    db.refresh(r)
    return (r)

def get_all_records(db: Session):
    return db.query(models.Person_Record).all()


def filter_record_by_name(db: Session, name: str):
    n = str(name).upper()
    return db.query(
        models.Person_Record).filter(models.Person_Record.nombre == n).first()


def filter_record_by_name_all(db: Session, name: str):
    n = str(name).upper()
    return db.query(models.Person_Record).filter(
        models.Person_Record.nombre.contains(n)).all()


def filter_record_by_last_name(db: Session, last_name: str):
    n = str(last_name).upper()
    return db.query(models.Person_Record).filter(
        models.Person_Record.apellido.contains(n)).first()


def filter_record_by_last_name_all(db: Session, last_name: str):
    n = str(last_name).upper()
    return db.query(models.Person_Record).filter(
        models.Person_Record.apellido.contains(n)).all()


def filter_record_by_ci(db: Session, ci: str):
    n = str(ci)
    return db.query(
        models.Person_Record).filter(models.Person_Record.cedula == n).first()


def filter_record_if_contains_ci(db: Session, ci: str):
    n = str(ci)
    return db.query(models.Person_Record).filter(
        models.Person_Record.cedula.contains(n)).all()


def filter_record_by_application_date(db: Session, date: str):
    return db.query(models.Person_Record).filter(
        models.Person_Record.fecha_aplicacion == date).all()


def filter_record_by_application_date_restricted(db: Session, date: str,
                                                 cant: int):
    data = db.query(models.Person_Record).filter(
        models.Person_Record.fecha_aplicacion == date).limit(cant).all()
    return (data)
