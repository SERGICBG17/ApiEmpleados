from sqlmodel import SQLModel,Field,Relationship

class Sede(SQLModel, table=True):
    id:int | None =Field(default=None,primary_key=True)
    nombre:str
    direccion: str |None=None

    departamentos:list["Departamento"] =Relationship(back_populates="sede")