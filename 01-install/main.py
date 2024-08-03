from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "FastAPI - Docs"
app.version = "0.0.1"

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

@app.get('/movies', tags=['Movies'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            return movie
    return {"error": "Movie not found"}

@app.get('/movies/', tags=['Movies'])
def get_movies_by_category(category: str):
    return [movie for movie in movies if movie["category"] == category]