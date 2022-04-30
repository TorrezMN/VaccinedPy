#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

import sys

import Base
import db_connection
import import
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ../db_crud.db_connection import Base


class Person_Record(Base):
    __tablename__ = 'Person_Record'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), index=True)
    apellido = Column(String(50), index=True)
    fecha_aplicacion = Column(Date, index=True)
    cedula = Column(String(15), index=True)
    actualizado_al = Column(Date, index=True)
    establishment = Column(Integer, ForeignKey('Establishments.id'))
    dose = Column(Integer, ForeignKey('Dose.id'))
    vaccine = Column(Integer, ForeignKey('Vaccine.id'))
