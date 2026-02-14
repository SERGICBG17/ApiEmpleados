from sqlmodel import SQLModel, Field, Relationship

class Empleado(SQLModel, table=True):
    id: int | None =Field(default=None,primary_key=True)
    nombre:str
    apellido:str | None=None
    genero:str | None=None
    edad:int | None=None
    imagen_uri:str | None=None
    sueldo:float | None=None
    correo:str| None=None
    telefono:int |None=None
    departamento_id: int | None = Field(default=None, foreign_key="departamento.id")

    departamento:"Departamento"=Relationship(back_populates="empleados")
