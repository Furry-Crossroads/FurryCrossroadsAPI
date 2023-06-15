from app import db

from sqlalchemy.dialects.postgresql import (
    UUID, 
)
from sqlalchemy import (
    Column, ForeignKey,
    Integer, SmallInteger,Boolean, Text, DateTime, Float, String
)
import uuid
import secrets
import datetime



class DiscordMember(db.Model):
    __tablename__ = 'discord_members'
    discord_id          = Column(String(64), primary_key=True, nullable=False)
    member_registration = Column(UUID(as_uuid=True), ForeignKey('member.registration'), nullable=False)
    


