#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from db_engine.database import Base
from sqlalchemy import Boolean, Column, Integer, String, Date
from sqlalchemy.orm import relationship

#  MODELS
#  ==========================
#  'establecimiento',
#  'dosis',
#  'descripcion_vacuna',


class Establishments(Base):
    __tablename__ = 'Establishments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    establishments_name = Column(String, unique=True, index=True)


class Dose(Base):
    __tablename__ = 'Dose'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dose_number = Column(String, unique=True, index=True)


class Vaccine(Base):
    __tablename__ = 'Vaccine'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vaccine_name = Column(String, unique=True, index=True)


#  REGISTRO
#  ==========================
#  'nombre'
#  'apellido'
#  'establecimiento'
#  'fecha_aplicacion'
#  'cedula'
#  'dosis'
#  'descripcion_vacuna'
#  'actualizado_al'


class Person_Record(Base):
    __tablename__ = 'Person_Record'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), index=True)
    apellido = Column(String(50), index=True)
    establecimiento = relationship('Establishments',
                                   foreign_keys='Establishments.id')
    fecha_aplicacion = Column(Date, index=True)
    cedula = Column(String(9), index=True)
    dosis = relationship('Dose', foreign_keys='Dose.id')
    descripcion_vacuna = relationship('Vaccine', foreign_keys='Vaccine.id')
    actualizado_al = Column(Date, index=True)
