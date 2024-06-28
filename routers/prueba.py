from fastapi import APIRouter, Request
from fastapi import  Path, Query, Depends
from fastapi.responses import  JSONResponse

prueba_router = APIRouter()

@prueba_router.post('/prueba', tags=['prueba'])
def prueba(request: Request):
    data = request.json()
    prueba_data = data.get("prueba")
    print(prueba_data)
    return JSONResponse(status_code=200, content={"message": "prueba recibida correctamente"})
