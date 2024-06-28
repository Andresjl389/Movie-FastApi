from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from middlewares.jwt_bearer import JwtBearer
from routers.movie import movie_router
from routers.login import login_router
from routers.projects import Projects
from routers.prueba import prueba_router
from fastapi.middleware.cors import CORSMiddleware

from routers.stack import TechStack


app = FastAPI()
app.title = "Mi aplicación con FastApi"
app.version = "0.0.3"

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(login_router)
app.include_router(prueba_router)
app.include_router(TechStack)
app.include_router(Projects)



Base.metadata.create_all(bind=engine)


    
    
movies = [
    {
        'id': 1,
        'title': "Avatar",
        'overview': "En un exuberante planeta llamdo Pandora viven los ... ",
        'year': "2009",
        'rating': 7.8,
        'category': 'Acción'
    },
    {
        'id': 2,
        'title': "Avatar",
        'overview': "En un exuberante planeta llamdo Pandora viven los ... ",
        'year': "2019",
        'rating': 7.8,
        'category': 'Accion'
    }
]



@app.get("/",tags=["Home"])
def message():
    return HTMLResponse('<h1>Hello World</h1>')



