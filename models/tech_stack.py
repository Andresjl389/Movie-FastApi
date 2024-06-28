from sqlalchemy import Column, String
from config.database import Base
import uuid

class TechStackModel(Base):
    __tablename__ = 'tech_stack'

    id = Column(String, primary_key=True, default=str(uuid.uuid4))
    title = Column(String)
    description = Column(String)
    image = Column(String)
