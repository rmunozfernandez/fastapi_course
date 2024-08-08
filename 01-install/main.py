from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()
app.title = "FastAPI - Docs"
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=1, max_length=50)
    overview: str = Field(min_length=1, max_length=50)
    year: int = Field(gt=1900, lt=2022)
    rating: float = Field(ge=0.0, le=10.0)
    category: str = Field(min_length=1, max_length=20)

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "title": "Película",
                "overview": "Descripción",
                "year": 2000,
                "rating": 0.0,
                "category": "Categoria"
            }
        }
    }

movies = [
    {
        "id": 1,
        "title": "The Shawshank Redemption",
        "overview": "Two imprisoned",
        "year": 1994,
        "rating": 9.3,
        "category": "Drama"
    },
    {
        "id": 2,
        "title": "The Godfather",
        "overview": "The aging patriarch",
        "year": 1972,
        "rating": 9.2,
        "category": "Crimen"
    },
    {
        "id": 3,
        "title": "The Dark Knight",
        "overview": "When the menace",
        "year": 2008,
        "rating": 9.0,
        "category": "Acción"
    },
]

@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1>Welcome to FastAPI</h1>')

@app.get('/movies', tags=['Movies'], response_model=list[Movie])
def get_movies() -> list[Movie]:
    return JSONResponse(content=movies)

@app.get('/movies/{id}', tags=['Movies'], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=200)) -> Movie:
    for mov in movies:
        if mov["id"] == id:
            return JSONResponse(content=mov)
    return JSONResponse(content={"error": "Movie not found"})

@app.get('/movies/', tags=['Movies'], response_model=list[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> list[Movie]:
    data = [mov for mov in movies if mov["category"] == category]
    return JSONResponse(content=data)

@app.post('/movies', tags=['Movies'], response_model=dict)
def create_movie(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(content={"message": "Movie created"})

@app.put('/movies/{id}', tags=['Movies'], response_model=dict)
def update_movie(id: int, movie: Movie) -> dict:
    for mov in movies:
        if mov["id"] == id:
            mov["title"] = movie.title
            mov["overview"] = movie.overview
            mov["year"] = movie.year
            mov["rating"] = movie.rating
            mov["category"] = movie.category
            return JSONResponse(content={"message": "Movie updated"})
    return JSONResponse(content={"error": "Movie not found"})

@app.delete('/movies/{id}', tags=['Movies'], response_model=dict)
def delete_movie(id: int) -> dict:
    for mov in movies:
        if mov["id"] == id:
            movies.remove(mov)
            return JSONResponse(content={"message": "Movie deleted"})
    return JSONResponse(content={"error": "Movie not found"})