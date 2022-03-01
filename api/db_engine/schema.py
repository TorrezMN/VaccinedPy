#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN


from datetime import date
from typing import Optional

from pydantic import BaseModel


class Establishments(BaseModel):
    establishments_name : str
    class Config:
        orm_mode = True


class Dose(BaseModel):
    dose_number : str 
    class Config:
        orm_mode = True

class Vaccine(BaseModel):
    vaccine_name: str 
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
