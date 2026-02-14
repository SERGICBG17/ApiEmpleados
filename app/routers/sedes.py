from fastapi import APIRouter, Depends
from app.services.sede_service import SedeService
from app.schemas.sede import SedeCreate, SedeResponse, SedeUpdate

router = APIRouter(prefix="/sedes", tags=["Sedes"])

@router.post("/", response_model=SedeResponse)
async def create_sede(sede: SedeCreate,service: SedeService = Depends()):
    return service.create(sede)

@router.get("/", response_model=list[SedeResponse])
async def read_sedes(service: SedeService = Depends()):
    return service.get_all()

@router.get("/{id}", response_model=SedeResponse)
async def read_sede(id: int, service: SedeService = Depends()):
    return service.get_by_id(id)

@router.patch("/{id}", response_model=SedeResponse)
async def update_sede(id: int,sede_data: SedeUpdate,service: SedeService = Depends()):
    return service.update(id, sede_data)

@router.delete("/{id}", response_model=dict)
async def delete_sede(id: int, service: SedeService = Depends()):
    return service.delete(id)