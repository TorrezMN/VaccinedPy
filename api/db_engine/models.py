#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from db_engine.database import Base
from sqlalchemy import Boolean, Column, Integer, String

#  MODELS
#  ==========================
#  'establecimiento',
#  'dosis',
#  'descripcion_vacuna',


class Establishments(Base):
    __tablename__ = 'Establishments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    establishments_name = Column(String, unique=True)


class Dose(Base):
    __tablename__ = 'Dose'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dose_number = Column(String, unique=True)


class Vaccine(Base):
    __tablename__ = 'Vaccine'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vaccine_name = Column(String, unique=True)
