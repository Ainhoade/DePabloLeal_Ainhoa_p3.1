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