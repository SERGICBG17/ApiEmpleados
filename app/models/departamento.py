from sqlmodel import SQLModel, Field, Relationship

class Departamento(SQLModel, table=True):
    id:int | None =Field(default=None,primary_key=True)
    nombre:str
    correo:str| None=None
    telefono:int |None=None
    ganancias:float |None=None

    sede_id: int | None = Field(default=None, foreign_key="sede.id")

    empleados:list["Empleado"]=Relationship(back_populates="departamento")
    sede:"Sede"=Relationship(back_populates="departamentos")
