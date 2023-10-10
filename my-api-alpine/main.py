from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from datos import MOVIES as movies
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token

# creando una instancia de FastAPI
app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"

class User(BaseModel):
    username: str
    email: str
    password: str


class Movie(BaseModel):
    id: int | None = None
#    id: Optional[int] = None
    title: str = Field(default='movie title', min_length=5, max_length=15)
    year: int = Field(default=2022, le=2022)
    rating: float = Field(default=0, ge=0, le=10)
    category: str = Field(default='movie category') 

    # Esta clase no sirve
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi película",
                "year": 2022,
                "rating": 9.8,
                "category" : "Acción"
            }
        }



@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello-Cruel-World</h1>')


@app.post('/login', tags=['auth'], status_code=201)
def login(user: User):
    if user.username == "platzi" and user.password == "root":
        token: str = create_token(user.dict())
        return JSONResponse(content={"message": "user authorized",
                                 "username": user.username,
                                 "token": token}, status_code=201)
    
    return JSONResponse(content={"message": "Not Authorized"}, status_code=401)


@app.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200)
def get_movies() -> List[Movie]:
    return JSONResponse(content=movies, status_code=200)


@app.get('/movies/{id}', tags=['movies'], response_model=Movie, status_code=200)
def get_movie(id: int = Path(ge=0, le=200)) -> Movie:
    for item in movies:
        if item['id'] == id:
            print(id)
            return JSONResponse(content=item, status_code=200)
        
    return JSONResponse(content={"message": "Movie Not Found"}, status_code=404)


@app.get('/movies/', tags=['movies'], response_model=List[Movie], status_code=200)
def get_movies_by_category(category: str = Query(min_length=5)) -> List[Movie]:
    movies_by_cat = [movie for movie in movies if movie['category'] == category]

    return JSONResponse(content=movies_by_cat, status_code=200)


@app.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:    
    movies.append(dict(movie))

    return JSONResponse(status_code=201, content={"message": "se ha creado la pelicula"})
   

@app.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            break
    return JSONResponse(content={"message": "se ha eliminado la pelicula",}, status_code=200)



@app.put('/movies/{id}', tags=['movies'], response_model=dict)
def update_movie(id: int, movie: Movie) -> dict:
    
    for item in movies:
        if item['id'] == id:            
            item['title'] = movie.title
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            break
    
    return JSONResponse(content={"message": "La película ha sido modificada", 
                                 "modified_id": item["id"]})



def not_found():
    pass
    return JSONResponse(content={"message": "NOT FOUND ERROR"})
