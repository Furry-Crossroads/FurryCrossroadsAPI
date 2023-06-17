from app import db

from sqlalchemy.dialects.postgresql import (
    UUID, 
    INTEGER, SMALLINT, BIGINT
)
from sqlalchemy import (
    Table, Column, ForeignKey, CheckConstraint,
    Integer, Boolean, Text, DateTime, Float, String
)
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime, timedelta

class OauthToken(db.Model):
    __tablename__ = 'oauth'
    oauth          = Column(String(64), primary_key=True, nullable=False)
    member_registration = Column(UUID(as_uuid=True), ForeignKey('member.registration'), nullable=False)
    time_generated = Column(DateTime, nullable=False, default=datetime.now())
    expires_at = Column(DateTime, nullable=False, default=datetime.now() + timedelta(minutes=30))
