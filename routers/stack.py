from uuid import UUID
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from models.tech_stack import TechStackModel
from config.database import Session
from schemas.stack import TechStackCreateSchema
from services.stack import TechStackService

TechStack = APIRouter()

@TechStack.post('/add_tech_stack' ,  tags=['Stack'], response_model=TechStackCreateSchema)
async def add_tech_stack(stack: TechStackCreateSchema) -> TechStackModel:
    db = Session()
    # print(stack)
    TechStackService(db).add_stack(stack)
    print(stack)
    return JSONResponse(status_code=201, content={'message': 'Se ha agregado la tecnología'})

@TechStack.get('/get_tech_stack', tags=['Stack'], response_model=list[TechStackCreateSchema])
async def get_tech_stack():
    db = Session()
    result = TechStackService(db).get_tech_stack()
    return result

@TechStack.delete('/delete_tech_stack/{id}', tags=['Stack'], response_model=TechStackCreateSchema)
async def delete_tech_stack(id: UUID) -> TechStackCreateSchema:
    db = Session()
    result = TechStackService(db).delete_tech_stack(id)
    return result

@TechStack.put('/update_stack/{id}', tags=['Stack'], response_model=TechStackCreateSchema)
async def update_stack(id:UUID, data: TechStackCreateSchema):
    db = Session()
    result = TechStackService(db).update_stack(id, data)
    return result