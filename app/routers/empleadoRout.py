from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_session
from app.services.empleadoService import EmpleadoService
from app.schemas.empleadoSchema import EmpleadoCreate, EmpleadoResponse, EmpleadoUpdate

router = APIRouter(prefix = "/empleados", tags = ["Empleados"])

@router.post("/", response_model=EmpleadoResponse)
async def create_empleado(empleado: EmpleadoCreate, service: EmpleadoService = Depends()):
    return service.create(empleado)




