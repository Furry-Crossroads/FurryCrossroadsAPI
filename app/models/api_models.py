from app import db

from sqlalchemy.dialects.postgresql import (
    UUID, 
)
from sqlalchemy import (
    Column, ForeignKey,
    Integer, SmallInteger,Boolean, Text, DateTime, Float, String
)
import uuid


class ApiToken(db.Model):
    __tablename__ = 'api_tokens'
    token               = Column(String(64), primary_key=True, nullable=False)
    member_registration = Column(UUID(as_uuid=True), ForeignKey('member.registration'), nullable=False)
    generated_at        = Column(DateTime, nullable=False, default=db.func.now())
    expiration          = Column(DateTime, nullable=False, default=db.func.now() + db.func.cast('1 day', DateTime))
    active              = Column(Boolean, nullable=False, default=True)


class Logs(db.Model):
    __tablename__ = 'logs'

    # Make the log_id an autoincrement integer
    log_id          = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # Whether it was a member login or an api token request.
    authorization   = Column(Text, nullable=True)
    ip_address      = Column(Text, nullable=True)
    endpoint        = Column(Text, nullable=True)
    method          = Column(Text, nullable=True)
    duration        = Column(SmallInteger, nullable=True)
    timestamp       = Column(DateTime, nullable=True, default=db.func.now())
    status          = Column(SmallInteger, nullable=True)
    host            = Column(Text, nullable=True)
    params          = Column(Text, nullable=True)
    useragent       = Column(Text, nullable=True)

