#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN


from typing import Optional

from pydantic import BaseModel


class DeviceInfo(BaseModel):
    token: str
    username: Optional[str]

    class Config:
        orm_mode = True


class Configuration(BaseModel):
    modelUrl: str
    frequency: int
    federated: bool

    class Config:
        orm_mode = True
