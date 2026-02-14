from fastapi import APIRouter, Depends
from app.services.departamento_service import DepartamentoService
from app.schemas.departamento import (DepartamentoCreate,DepartamentoResponse,DepartamentoUpdate,)

# Definimos el router con un prefijo para todas las rutas
router = APIRouter(prefix="/departamentos", tags=["Departamentos"])

@router.post("/", response_model=DepartamentoResponse)
async def create_departamento(departamento: DepartamentoCreate,service: DepartamentoService = Depends()):
    return service.create(departamento)

@router.get("/", response_model=list[DepartamentoResponse])
async def read_departamentos(service: DepartamentoService = Depends()):
    return service.get_all()

@router.get("/{id}", response_model=DepartamentoResponse)
async def read_departamento(id: int, service: DepartamentoService = Depends()):
    return service.get_by_id(id)

@router.patch("/{id}", response_model=DepartamentoResponse)
async def update_departamento(id: int,departamento_data: DepartamentoUpdate,service: DepartamentoService = Depends()):
    return service.update(id, departamento_data)

@router.delete("/{id}", response_model=dict)
async def delete_departamento(id: int, service: DepartamentoService = Depends()):
    return service.delete(id)