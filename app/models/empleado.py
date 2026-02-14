
from sqlmodel import SQLModel, Field, Relationship

class Empleado(SQLModel, table=True):
    nombre:           str 
    apellido:         str 
    telefono:         str 
    fecha_nacimiento: int 
    direccion:        str 
    imagen_empleado:  str | None = None

    id: int | None = Field(default = None, primary_key = True) 
    departamentos: list["Departamento"]  = Relationship(back_populates = "empleado", cascade_delete = True)