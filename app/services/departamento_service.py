from sqlmodel import Session, select
from fastapi import Depends, HTTPException
from app.models.departamento import Departamento
from app.schemas.departamento import (DepartamentoCreate,DepartamentoResponse,DepartamentoUpdate)
from app.db.session import get_session

class DepartamentoService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, data: DepartamentoCreate) -> DepartamentoResponse:
        dept = Departamento(**data.model_dump())
        self.session.add(dept)
        self.session.commit()
        self.session.refresh(dept)
        return DepartamentoResponse(**dept.model_dump())

    def get_all(self):
        return self.session.exec(select(Departamento)).all()

    def get_by_id(self, id: int):
        dept = self.session.get(Departamento, id)
        if not dept:
            raise HTTPException(status_code=404, detail="Departamento no encontrado")
        return dept

    def update(self, id: int, data: DepartamentoUpdate):
        dept = self.session.get(Departamento, id)
        if not dept:
            raise HTTPException(status_code=404, detail="Departamento no encontrado")

        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(dept, key, value)

        self.session.add(dept)
        self.session.commit()
        self.session.refresh(dept)
        return dept

    def delete(self, id: int):
        dept = self.session.get(Departamento, id)
        if not dept:
            raise HTTPException(status_code=404, detail="Departamento no encontrado")
        self.session.delete(dept)
        self.session.commit()
        return {"message": "Departamento eliminado"}