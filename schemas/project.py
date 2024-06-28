from typing import Optional
from pydantic import BaseModel, Field
import uuid

class ProjectSchema(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    title: str = Field(min_length=1, max_length=50)
    description: str = Field(min_length=10, max_length=1000)
    image: str = Field(min_length=10, max_length=1000)

    class Config:
        json_schema_extra = {
            'example':{
                'title': 'LocalFood',
                'description': 'Projecto creado python usando solamente el framework de Django con javascript',
                'image': '/path/to/image.jpg',
            }
        }
