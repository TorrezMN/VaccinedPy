#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from datetime import date
from typing import Optional

from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://username:password@db:5432/nudges"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def db_inspector():
    inspector = inspect(engine)
    schemas = inspector.get_schema_names()
    print('TABLE NAMES ->', inspector.get_table_names())
    print('INSPECTOR ->', dir(inspector))
    print({'SCHEMAS -> ': schemas})
