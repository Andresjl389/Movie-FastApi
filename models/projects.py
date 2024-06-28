from sqlalchemy import Column, String, LargeBinary
from config.database import Base
import uuid

class ProjectsModel(Base):
    __tablename__ = 'Projects'

    id = Column(String, primary_key=True, default=str(uuid.uuid4))
    title = Column(String)
    description = Column(String)
    image = Column(LargeBinary)