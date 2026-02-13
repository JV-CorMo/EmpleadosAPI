from  sqlmodel import SQLModel

class EmpleadoCreate(SQLModel):
    nombre:           str 
    apellido:         str 
    telefono:         str 
    fecha_nacimiento: int 
    direccion:        str 
    imagen_empleado:  str | None = None

class EmpleadoResponse(EmpleadoCreate):
    id: int 

class EmpleadoUpdate(SQLModel):
    nombre:           str 
    apellido:         str 
    telefono:         str 
    fecha_nacimiento: int 
    direccion:        str 
    imagen_empleado:  str | None = None