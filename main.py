from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API de Juegos de Mesa")

# Modelos 

class BoardGameBase(BaseModel):
    name: str
    players: int
    duration: int
    cooperative: bool
    categories: List[str]


class BoardGame(BoardGameBase):
    id: int

boardgames_db: List[BoardGame] = []

# Crear un juego de mesa
@app.post("/boardgames", response_model=BoardGame, status_code=201)
def create_boardgame(game: BoardGame):
    for g in boardgames_db:
        if g.id == game.id:
            #Errores personalizados
            raise HTTPException(
                status_code=400,
                detail="El juego de mesa ya existe"
            )
    boardgames_db.append(game)
    return game

# Obtener todos los juegos
@app.get("/boardgames", response_model=List[BoardGame])
def get_boardgames():
    return boardgames_db

# Obtener un juego por ID
@app.get("/boardgames/{game_id}", response_model=BoardGame)
def get_boardgame(game_id: int):
    for game in boardgames_db:
        if game.id == game_id:
            return game
    raise HTTPException(
        #Errores personalizados
        status_code=404,
        detail="Juego de mesa no encontrado"
    )

# Actualizar un juego
@app.put("/boardgames/{game_id}", response_model=BoardGame)
def update_boardgame(game_id: int, updated_game: BoardGameBase):
    for index, game in enumerate(boardgames_db):
        if game.id == game_id:
            new_game = BoardGame(
                id=game_id,
                **updated_game.dict()
            )
            boardgames_db[index] = new_game
            return new_game

    raise HTTPException(
        status_code=404,
        detail="Juego de mesa no encontrado"
    )

# Eliminar un juego
@app.delete("/boardgames/{game_id}", status_code=204)
def delete_boardgame(game_id: int):
    for game in boardgames_db:
        if game.id == game_id:
            boardgames_db.remove(game)
            return

    raise HTTPException(
        status_code=404,
        detail="Juego de mesa no encontrado"
    )