from fastapi import APIRouter, Depends, File, UploadFile

from sqlmodel import Session
from app.db.session import get_session
from app.services.empleadoService import EmpleadoService
from app.schemas.empleadoSchema import EmpleadoCreate, EmpleadoResponse, EmpleadoUpdate


router = APIRouter(prefix = "/empleados", tags = ["Empleado"])

@router.post("/", response_model=EmpleadoResponse)
async def create_empleado(empleado: EmpleadoCreate, service: EmpleadoService = Depends()):
    return service.create(empleado)

@router.get("/", response_model=list[EmpleadoResponse])
async def read_empleados(service: EmpleadoService = Depends()):
    return service.get_all()

@router.get("/{id}", response_model=EmpleadoResponse)
async def read_empleado(id: int, service: EmpleadoService = Depends()):
    return service.get_by_id(id)

@router.patch("/{id}", response_model=EmpleadoResponse)
async def read_empleado(id: int, empleado_data: EmpleadoResponse, service: EmpleadoService = Depends()):
    return service.update(id, empleado_data)

@router.delete("/{id}", response_model=dict)
async def delete_empleado(id: int, service: EmpleadoService = Depends()):
    return service.delete(id)

@router.post("/{id}/imagen", response_model=EmpleadoResponse)
async def up_imagen_empleado(id: int,imagen: UploadFile = File(...), service: EmpleadoService = Depends()):
    return service.up_imagen_empleado(id, imagen)
    

