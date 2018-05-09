from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Date, Boolean, func
from datetime import datetime, timedelta
from selfservice import db


class ResetToken(db.Model):
    __tablename__ = 'token'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False)
    created = Column(DateTime, default=func.current_timestamp())


class RecoverySession(db.Model):
	__tablename__ = 'session'
	id = Column(String(36), primary_key=True)
	username = Column(String(64), nullable=False)
	created = Column(DateTime, default=func.current_timestamp())


class PhoneVerification(db.Model):
	__tablename__ = 'phone_codes'
	username = Column(String(64), primary_key=True)
	code = Column(String(6), primary_key=True)
