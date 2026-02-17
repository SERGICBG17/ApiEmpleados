from sqlmodel import SQLModel

class EmpleadoCreate(SQLModel):
    nombre:str
    apellido:str
    genero:str | None=None
    edad:int | None=None
    imagen_uri:str | None=None
    sueldo:float  | None=None
    correo:str| None=None
    telefono:int |None=None
    departamento_id: int

class EmpleadoResponse(EmpleadoCreate):
    id: int

class EmpleadoUpdate(SQLModel):
    nombre:str | None=None
    apellido:str | None=None
    genero:str | None=None
    edad:int | None=None
    imagen_uri:str | None=None
    sueldo:float  | None=None
    correo:str| None=None
    telefono:int |None=None
    departamento_id:int | None=None