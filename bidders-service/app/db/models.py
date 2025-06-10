from sqlalchemy import Column, Integer, String, Boolean
from app.db.session import Base

class Bidder(Base):
    __tablename__ = "bidders"

    user_id = Column(Integer, primary_key=True, index=True)
    email_encrypted = Column("email", String, unique=True, nullable=False)
    password_hash = Column("password", String, nullable=False)
    is_verified = Column(Boolean, default=False)

    @property
    def email(self):
        from app.security.crypto import decrypt_email
        return decrypt_email(self.email_encrypted)

    @email.setter
    def email(self, plain_email: str):
        from app.security.crypto import encrypt_email
        self.email_encrypted = encrypt_email(plain_email)
