from contextlib import closing
from datetime import datetime
import os
import sqlite3
from sys import platform
from typing import Optional

from fastapi import FastAPI
from sqlmodel import Field, select, Session, SQLModel, create_engine


class RequestLog(SQLModel, table=True):
    __tablename__: str = "request_log"
    id: Optional[int] = Field(default=None, primary_key=True)
    path: str
    time: datetime

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

DBPATH = "../docker/" # local dev on my mac
if platform == "linux": # run app in docker
    # docker run should pass -v $name:/home to persist this
    DBPATH = "/home/"
    # why not use same path for mac?
    # => can't write to root
    # why not symlink?
    # => synthetic.conf is ~finnicky~
    # (bricks machine if does not end in newline)
DBFILE = "ffdb.db"

connect_args = {"check_same_thread": False}
engine = create_engine(f"sqlite:///{DBPATH}{DBFILE}", connect_args=connect_args)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/favicon.ico") # trap this
def foo():
    pass

@app.get("/show")
def show():
    with Session(engine) as session:
        return session.exec(select(RequestLog)).all()

# stop writing to db until there's auth in place
"""
@app.get("/{var}")
def sayhello(var: str):
    rec = RequestLog(path=var, time=datetime.now())
    with Session(engine) as session:
        session.add(rec)
        session.commit()
    return {"hello": var}
"""
