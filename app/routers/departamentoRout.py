from fastapi import APIRouter, Depends, Query
from app.services.departamentoService import DepartamentoServicio
from app.schemas.departamentoSchema import DepartamentoCreate, DepartamentoResponse, DepartamentoUpdate

router = APIRouter(prefix="/departamentos", tags=["Departamentos"])

@router.post("/", response_model=DepartamentoResponse)
async def create_departamento(departamento: DepartamentoCreate, service: DepartamentoServicio = Depends()):
    return service.create(departamento)

@router.get("/", response_model=list[DepartamentoResponse])
async def read_departamentos(service: DepartamentoServicio = Depends(),
    empleado_id: int | None = Query(None, description="Filtrar por ID del empleado")):
    return service.get_all(empleado_id)

@router.get("/{id}", response_model=DepartamentoResponse)
async def read_departamento(id: int, service: DepartamentoServicio = Depends()):
    return service.get_by_id(id)

@router.patch("/{id}", response_model=DepartamentoResponse)
async def update_departamento(id: int, departamento_data: DepartamentoUpdate, service: DepartamentoServicio = Depends()):
    return service.update(id, departamento_data)

@router.delete("/{id}", response_model=dict)
async def delete_departamento(id: int, service: DepartamentoServicio = Depends()):
    return service.delete(id)