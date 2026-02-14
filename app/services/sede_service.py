from sqlmodel import Session, select
from fastapi import Depends, HTTPException
from app.models.sede import Sede
from app.schemas.sede import SedeCreate, SedeResponse, SedeUpdate
from app.db.session import get_session

class SedeService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, data: SedeCreate) -> SedeResponse:
        sede = Sede(**data.model_dump())
        self.session.add(sede)
        self.session.commit()
        self.session.refresh(sede)
        return SedeResponse(**sede.model_dump())

    def get_all(self):
        return self.session.exec(select(Sede)).all()

    def get_by_id(self, id: int):
        sede = self.session.get(Sede, id)
        if not sede:
            raise HTTPException(status_code=404, detail="Sede no encontrada")
        return sede

    def update(self, id: int, data: SedeUpdate):
        sede = self.session.get(Sede, id)
        if not sede:
            raise HTTPException(status_code=404, detail="Sede no encontrada")

        # Solo actualizamos los campos que vienen en la petición
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(sede, key, value)

        self.session.add(sede)
        self.session.commit()
        self.session.refresh(sede)
        return sede

    def delete(self, id: int):
        sede = self.session.get(Sede, id)
        if not sede:
            raise HTTPException(status_code=404, detail="Sede no encontrada")
        self.session.delete(sede)
        self.session.commit()
        return {"message": "Sede eliminada"}