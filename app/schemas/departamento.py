from sqlmodel import SQLModel

class DepartamentoCreate(SQLModel):
    nombre: str
    correo:str| None=None
    telefono:int |None=None
    ganancias:float |None=None
    sede_id: int

class DepartamentoResponse(DepartamentoCreate):
    id: int

class DepartamentoUpdate(SQLModel):
    nombre:str | None=None
    correo:str| None=None
    telefono:int |None=None
    ganancias:float |None=None
    sede_id: int | None=None