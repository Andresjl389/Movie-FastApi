from pydantic import BaseModel, Field
import uuid

class TechStackCreateSchema(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    title: str = Field(min_length=1, max_length=50)
    description: str = Field(min_length=10, max_length=1000)
    image: str = Field(min_length=5, max_length=1000)

    class Config:
        json_schema_extra = {
            'example':{
                'title': 'React.js',
                'description': 'Que es React.js',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1200px-React-icon.svg.png'
            }
        }
