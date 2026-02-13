from sqlmodel import Session, select
from fastapi import Depends, HTTPException
from app.models.empleado import Empleado
from app.schemas.empleadoSchema import EmpleadoCreate, EmpleadoResponse, EmpleadoUpdate
from app.db.session import get_session

class EmpleadoService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, empleado_data: EmpleadoCreate) -> EmpleadoResponse:
        empleado = Empleado(**empleado_data.model_dump())        
        self.session.add(empleado)
        self.session.commit()
        self.session.refresh(empleado)
        return EmpleadoResponse(**empleado.model_dump())
    
    def get_all(self):
        return self.session.exec(select(Empleado)).all()
    
    def get_by_id(self, id: int):
        return self.session.get(Empleado, id)
    
    def update(self, id: int, empleado_data: EmpleadoUpdate) -> Empleado:
        empleado = self.session.get(Empleado, id) 
        if not empleado:
            raise HTTPException(status_code = 404, detail = "No se encontro este empleado." ) 
        empleado_dict = empleado_data.model_dump(exclude_unset = True)
        for key, value in empleado_dict.items():
            setattr(empleado, key, value)

        self.session.add(empleado)
        self.session.commit()
        self.session.refresh(empleado)
        return empleado
    
    def delate(self, id: int):
        empleado = self.session.get(Empleado, id)
        if not empleado:
            raise HTTPException(status_code = 404, detail = "No se a encontrado empleado")
        self.session.delete(empleado)
        self.session.commit()
        return {"message": "Empleado eliminado exitosamente"}
        