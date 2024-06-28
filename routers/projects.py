import os
from uuid import UUID
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from models.projects import ProjectsModel
from config.database import Session
from schemas.project import ProjectSchema
from services.projects import ProjectsService
from os import getcwd


Projects = APIRouter()

@Projects.post('/add_project',tags=['Project'] , response_model=ProjectSchema)
async def add_project(data: ProjectSchema, file: UploadFile = File(...) ) -> ProjectSchema:
    db = Session()
    try:
        print('FILE NAME',file.filename)
        file_path = os.path.join('images', file.filename)
        print('FILE PATH',file_path)
        with open(file_path, 'wb' ) as myfile:
            content = await file.read()
            myfile.write(content)
            myfile.close()
    except FileNotFoundError:
        return JSONResponse(content={'message': 'File not found'}, status_code=404)
    print('DATOS A MANDAR',data, "FILE NAME", file )
    # ProjectsService(db).add_project(data, file.filename)
    return JSONResponse(status_code=201, content={'message': 'Se ha agregado el projecto'})

@Projects.get('/get_projects', tags=['Project'],response_model=list[ProjectSchema])
async def get_projects():
    db = Session()
    result = ProjectsService(db).get_projects()
    return result

@Projects.delete('/delete_project/{id}', tags=['Project'],response_model=ProjectSchema)
async def delete_tech_stack(id: UUID) -> ProjectSchema:
    db = Session()
    result = ProjectsService(db).delete_project(id)
    return result