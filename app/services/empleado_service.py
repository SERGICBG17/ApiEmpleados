from sqlmodel import Session, select
from fastapi import Depends, HTTPException
from app.models.empleado import Empleado
from app.schemas.empleado import EmpleadoCreate, EmpleadoResponse, EmpleadoUpdate
from app.db.session import get_session

class EmpleadoService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, data: EmpleadoCreate) -> EmpleadoResponse:
        emp = Empleado(**data.model_dump())
        self.session.add(emp)
        self.session.commit()
        self.session.refresh(emp)
        return EmpleadoResponse(**emp.model_dump())

    def get_all(self, departamento_id: int | None = None):
        query = select(Empleado)
        if departamento_id:
            query = query.where(Empleado.departamento_id == departamento_id)
        return self.session.exec(query).all()

    def get_by_id(self, id: int):
        emp = self.session.get(Empleado, id)
        if not emp:
            raise HTTPException(status_code=404, detail="Empleado no encontrado")
        return emp

    def update(self, id: int, data: EmpleadoUpdate):
        emp = self.session.get(Empleado, id)
        if not emp:
            raise HTTPException(status_code=404, detail="Empleado no encontrado")

        # Solo actualizamos los campos que vienen en la petición
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(emp, key, value)

        self.session.add(emp)
        self.session.commit()
        self.session.refresh(emp)
        return emp

    def delete(self, id: int):
        emp = self.session.get(Empleado, id)
        if not emp:
            raise HTTPException(status_code=404, detail="Empleado no encontrado")
        self.session.delete(emp)
        self.session.commit()
        return {"message": "Empleado eliminado"}