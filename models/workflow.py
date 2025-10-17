from sqlalchemy import Column, Integer, String, Boolean, Text
from database import Base 

class Workflow(Base):
    __tablename__ = "workflows"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    policy = Column(Text)
    escalation = Column(Boolean, default=False)
