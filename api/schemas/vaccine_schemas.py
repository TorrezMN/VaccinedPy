#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN


from datetime import date
from typing import Optional

from pydantic import BaseModel


class Vaccine(BaseModel):
    vaccine_name: str 
    class Config:
        orm_mode = True

class Vaccine_Name(BaseModel):
    vaccine_name : str
    class Config:
        orm_mode = True
