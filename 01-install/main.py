from fastapi import FastAPI, Body
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

@app.post('/movies', tags=['Movies'])
def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return movies

@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    for movie in movies:
        if movie["id"] == id:
            movie["title"] = title
            movie["overview"] = overview
            movie["year"] = year
            movie["rating"] = rating
            movie["category"] = category
            return movie
    return {"error": "Movie not found"}

@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            return {"message": "Movie deleted"}
    return {"error": "Movie not found"}