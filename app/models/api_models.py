from app import db

from sqlalchemy.dialects.postgresql import (
    UUID, 
)
from sqlalchemy import (
    Column, ForeignKey,
    Integer, SmallInteger,Boolean, Text, DateTime, Float, String
)
import secrets
from datetime import datetime, timedelta

def generate_and_store_token(member_registration, expiration_days=30):
    # Generate a secure random token
    text_token = secrets.token_hex(32)

    # Determine the expiration date
    expires_at = datetime.utcnow() + timedelta(days=expiration_days)

    # Create a new ApiToken object
    token_model = ApiToken(
        token=text_token, 
        member_registration=member_registration, 
        expiration=expires_at,
        generated_at=datetime.utcnow(),
    )

    # Add the new token to the session and commit it
    db.session.add(token_model)
    db.session.commit()

    # Return the new token
    return text_token



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

