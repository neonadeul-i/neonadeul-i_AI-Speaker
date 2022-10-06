# coding: utf-8
from sqlalchemy import CHAR, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Ai(Base):
    __tablename__ = 'ai'

    seriaNamber = Column(CHAR(8), primary_key=True)


class Notice(Base):
    __tablename__ = 'notice'

    id = Column(Integer, primary_key=True)
    seriaNumber = Column(CHAR(8), nullable=False)
    content = Column(String(500), nullable=False)


class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    password = Column(String(16), nullable=False)
    type = Column(String(4), nullable=False)
    name = Column(String(4), nullable=False)
    phone = Column(CHAR(11), nullable=False)
    address = Column(String(11), nullable=False)


class Calendar(Base):
    __tablename__ = 'calendar'

    id = Column(Integer, primary_key=True)
    startdDay = Column(String(16), nullable=False)
    endDay = Column(String(16), nullable=False)
    title = Column(String(30), nullable=False)
    content = Column(String(700), nullable=False)
    user_id = Column(ForeignKey('user.id'), nullable=False, index=True)

    user = relationship('User')


class Helper(Base):
    __tablename__ = 'helper'

    id = Column(Integer, primary_key=True)
    startdDay = Column(CHAR(16), nullable=False)
    endDay = Column(CHAR(16), nullable=False)
    pay = Column(Integer, nullable=False)
    record = Column(String(1000), nullable=False)
    user_id = Column(ForeignKey('user.id'), nullable=False, index=True)

    user = relationship('User')


class Interlock(Base):
    __tablename__ = 'interlock'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('user.id'), nullable=False, index=True)
    seriaNamber = Column(ForeignKey('ai.seriaNamber'), nullable=False, index=True)

    ai = relationship('Ai')
    user = relationship('User')
