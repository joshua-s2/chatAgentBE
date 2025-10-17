from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from database import Base

class Session(Base):
    __tablename__ = "sessions"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)

    chats = relationship("Chat", back_populates="session", cascade="all, delete")
