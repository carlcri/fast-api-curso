from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse
from datos import MOVIES as movies
from pydantic import BaseModel, Field
from typing import Optional

# creando una instancia de FastAPI
app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"

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
    return HTMLResponse('<h1>Hello World</h1>')


@app.get('/movies', tags=['movies'])
def get_movies():
    return movies


@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int = Path(ge=0, le=200)):
    for item in movies:
        if item['id'] == id:
            print(id)
            return item
    return None


@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str = Query(min_length=5)):
    return [movie for movie in movies if movie['category'] == category]


@app.post('/movies', tags=['movies'])
def create_movie(movie: Movie):    
    movies.append(dict(movie))

    return movie
   

@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            break
    return id



@app.put('/movies/{id}', tags=['movies'], response_model=Movie)
def update_movie(id: int, movie: Movie):
    
    for item in movies:
        if item['id'] == id:            
            item['title'] = movie.title
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            break
    
    return item