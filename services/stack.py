from uuid import UUID

from fastapi.responses import JSONResponse
from models.tech_stack import TechStackModel
from schemas.stack import TechStackCreateSchema

class TechStackService:
    def __init__(self, db) -> None:
        self.db = db

    def add_stack(self, stack: TechStackCreateSchema):
        new_stack = TechStackModel(
            id=str(stack.id),
            title=stack.title,
            description=stack.description,
            image=stack.image,
        )
        print('DESDE EL SERVICE')
        print(new_stack.id)
        print(new_stack.title)
        print(new_stack.description)
        print(new_stack.image)
        self.db.add(new_stack)
        self.db.commit()


    def get_tech_stack(self):
        result = self.db.query(TechStackModel).all()
        return result
    
    def delete_tech_stack(self, id: UUID):
        result = self.db.query(TechStackModel).filter(TechStackModel.id == str(id)).first()
        print('DESDE EL SERVICE')
        print(id)
        print(result)
        if not result:
            return JSONResponse(status_code=404, content={'message': 'Stack not found'})
        else:
            self.db.delete(result)
            self.db.commit()
            return JSONResponse(status_code=200,content={"message":"Se ha eliminado la tecnología"})
        
    def update_stack(self, id: UUID, data: TechStackCreateSchema):
        update_stack = self.db.query(TechStackModel).filter(TechStackModel.id == str(id)).first()
        if not update_stack:
            return JSONResponse(status_code=404, content={'message': 'Stack not found'})
        

        update_stack.title = data.title
        update_stack.description = data.description
        update_stack.image = data.image
        self.db.commit()
        return JSONResponse(status_code=200,content={"message":"Se ha actualizado la tecnología"})