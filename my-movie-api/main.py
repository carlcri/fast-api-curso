from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from datos import MOVIES as movies
from pydantic import BaseModel
from typing import Optional

# creando una instancia de FastAPI
app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"

class Movie(BaseModel):
    id: int | None = None
#    id: Optional[int] = None
    title: str 
    year: int
    rating: float
    category: str


@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello World</h1>')


@app.get('/movies', tags=['movies'])
def get_movies():
    return movies


@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    for item in movies:
        if item['id'] == id:
            print(id)
            return item
    return None


@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str, year: int):
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