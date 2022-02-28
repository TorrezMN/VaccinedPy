#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from sqlalchemy.orm import Session
from db_engine import schema, models


def save_establishment(db: Session, info: schema.Establishments):
    est = models.Establishments(**info.dict())
    db.add(est)
    db.commit()
    db.refresh(est)
    return (est)


def save_dose(db: Session, info: schema.Dose):
    dose = models.Dose(**info.dict())
    db.add(dose)
    db.commit()
    db.refresh(dose)
    return (dose)


def get_all_establishments(db: Session):
    return db.query(models.Establishments).all()


def get_all_dose(db: Session):
    return db.query(models.Dose).all()


#
#  def save_device_info(db: Session, info: schema.DeviceInfo):
#  device_info_model = models.DeviceInfo(**info.dict())
#  db.add(device_info_model)
#  db.commit()
#  db.refresh(device_info_model)
#  return device_info_model
#
#
#  def get_device_info(db: Session, token: str = None):
#  if token is None:
#  return db.query(models.DeviceInfo).all()
#  else:
#  return db.query(models.DeviceInfo).filter(
#  models.DeviceInfo.token == token).first()
#
#
#  def save_nudges_configuration(db: Session, config: schema.Configuration):
#  config_model = models.Configuration(**config.dict())
#  db.add(config_model)
#  db.commit()
#  db.refresh(config_model)
#  return config_model
#
#
#  def get_nudges_configuration(db: Session):
#  return db.query(models.Configuration).first()
#
#
#  def delete_nudges_configuration(db: Session):
#  db.query(models.Configuration).delete()
#
#
def error_message(message):
    return {'error': message}
