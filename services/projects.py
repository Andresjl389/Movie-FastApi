from os import getcwd, path
from uuid import UUID
from fastapi.responses import JSONResponse
from models.projects import ProjectsModel
from schemas.project import ProjectSchema

class ProjectsService:
    def __init__(self, db) -> None:
        self.db = db

    async def add_project(self, data: ProjectSchema, image_data: bytes):

        image_filename = str(UUID()) + path.splitext(data.image.filename)[-1]
        image_path = path.join("static", "images", image_filename)
        with open(image_path, 'wb') as image_file:
            image_file.write(image_data)
        new_project = ProjectsModel(
            title=data.title,
            description=data.description,
            image=image_path
        )
        self.db.add(new_project)
        self.db.commit()


    def get_projects(self):
        result = self.db.query(ProjectsModel).all()
        return result
    
    def delete_project(self, id: UUID):
        result = self.db.query(ProjectsModel).filter(ProjectsModel.id == str(id)).first()
        print('DESDE EL SERVICE')
        print(id)
        print(result)
        if not result:
            return JSONResponse(status_code=404, content={'message': 'Stack not found'})
        else:
            self.db.delete(result)
            self.db.commit()
            return JSONResponse(status_code=200,content={"message":"Se ha eliminado la tecnología"})