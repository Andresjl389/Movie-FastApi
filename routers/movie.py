from fastapi import APIRouter
from fastapi import  Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  Optional, List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JwtBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()


@movie_router.get("/movies", tags=["Movies"], response_model=List[Movie], status_code=200)
def get_moovies() -> List[Movie]:
    db = Session()
    # result = db.query(MovieModel).all()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@movie_router.get("/movies/{id}",tags=["Movies"], response_model=Movie)
def get_movie(id:int = Path(ge=1, le=2000)) -> Movie:
    db = Session()
    # result = db.query(MovieModel).filter(MovieModel.id == id).first()
    result = MovieService(db).get_movies_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Movie not found'})
    # for item in movies:
    #     if item['id'] == id:
    #         return JSONResponse(content=item)
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@movie_router.get("/movies/", tags=["Movies"], response_model=List[Movie])
def get_movie_by_category(category:str = Query(min_length=5, max_length=15)) -> List[Movie]:
    # for data in movies:
    #     if data['category'] == category:
    #         return JSONResponse(content=data)

    db = Session()
    # result = db.query(MovieModel).filter(MovieModel.category == category).all()
    result = MovieService(db).get_category(category)

    if not result:
        return JSONResponse(status_code=404, content={'message': 'Category not found'})
    return JSONResponse(status_code=404,content=jsonable_encoder(result))

@movie_router.post("/movies", tags=["Movies"], response_model=dict, status_code=201)
def create_movie(movie:Movie) -> dict:
    db = Session()
    # new_Movie = MovieModel(**movie.dict())
    # db.add(new_Movie)
    # db.commit()

    MovieService(db).create_movie(movie)

    # movies.append(movie.model_dump())
    print(movie.model_dump())
    return JSONResponse(status_code=201,content={"message":"Se ha registrado la película"})


@movie_router.put('/movies/{id}',tags=["Movies"], response_model=dict, status_code=200)
def update_movie(id:int, movie:Movie) -> dict:
    db = Session()
    # result = db.query(MovieModel).filter(MovieModel.id == id).first()
    # if not result:
    #     return JSONResponse(status_code=404, content={'message': 'Movie not found'})
    # else: 
    #     result.title = movie.title
    #     result.overview = movie.overview
    #     result.year = movie.year
    #     result.rating = movie.rating
    #     result.category = movie.category
    #     db.commit()

    result = MovieService(db).get_movies_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Movie not found'})
     
    MovieService(db).update_movie(id, movie)

    return JSONResponse(status_code=200,content={"message":"Se ha modificado la película"})


    # for item in movies:
    #     if item['id'] == id:
    #         item['title'] = movie.title
    #         item['overview'] = movie.overview
    #         item['year'] = movie.year
    #         item['rating'] = movie.rating
    #         item['category'] = movie.category
    #         return JSONResponse(status_code=200,content={"message":"Se ha modificado la película"})

@movie_router.delete("/movies/{id}", tags=["Movies"], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    db = Session()
    # result = db.query(MovieModel).filter(MovieModel.id == id).first()
    result = MovieService(db).get_movies_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Movie not found'})
    # else:
    #     db.delete(result)
    #     db.commit()
    
    # for item in movies:
    #     if item['id'] == id:
    #         movies.remove(item)

    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=200,content={"message":"Se ha eliminado la película"})



