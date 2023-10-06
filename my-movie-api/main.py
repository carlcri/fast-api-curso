from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from datos import MOVIES as movies

# creando una instancia de FastAPI
app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"

# Primer END POINT
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
            return item
    return None


@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str, year: int):
    return [movie for movie in movies if movie['category'] == category]


@app.post('/movies', tags=['movies'])
def create_movie(id: int = Body(), 
                 title: str = Body(), 
                 year: int = Body(), 
                 rating: float = Body(), 
                 category: str= Body()):
    
    new_movie = dict(id = id,
                     title = title,
                     year = year,
                     rating = rating,
                     category = category)
    
    movies.append(new_movie)

    return [movie for movie in movies if movie['id'] == id]

@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            break
    return id



@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, 
                 title: str = Body(), 
                 year: int = Body(), 
                 rating: float = Body(), 
                 category: str= Body()):
    
    for movie in movies:
        if movie['id'] == id:
            
            movie['title'] = title
            movie['year'] = year
            movie['rating'] = rating
            movie['category'] = category
            break
    
    return id, title, year, rating, category