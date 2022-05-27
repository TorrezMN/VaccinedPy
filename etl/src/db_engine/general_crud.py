#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from db_engine import models
from sqlalchemy.orm import Session


def error_message(message):
    return {'error': message}
