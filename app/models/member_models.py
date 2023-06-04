from app import db

from sqlalchemy.dialects.postgresql import (
    UUID, 
    INTEGER, SMALLINT, BIGINT
)
from sqlalchemy import (
    Table, Column, ForeignKey, CheckConstraint,
    Integer, Boolean, Text, DateTime, Float, String
)
import uuid
from werkzeug.security import generate_password_hash, check_password_hash


class Member(db.Model):
    __tablename__ = 'member'

    registration      = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    role              = Column(
                            String(20), 
                            CheckConstraint(
                                "role IN ('member', 'mod', 'admin')", 
                                name='valid_role'
                            ),
                            nullable=False, 
                            default='member',
                        )

    username          = Column(String(32), nullable=True)
    pass_hash         = Column(db.String(128), nullable=True)

    bio               = Column(Text, nullable=True)
    registration_date = Column(DateTime, nullable=False, default=db.func.now())

    api_tokens        = db.relationship('ApiToken', backref='member', lazy=True)

    def set_password(self, password):
        self.pass_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pass_hash, password)