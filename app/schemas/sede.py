from sqlmodel import SQLModel

class SedeCreate(SQLModel):
    nombre:str
    direccion: str |None=None

class SedeResponse(SedeCreate):
    id: int

class SedeUpdate(SQLModel):
    nombre:str |None=None
    direccion: str |None=None