
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional



class Departamento(SQLModel, table = True):
    empleado_id: int = Field(foreign_key = "empleado.id")

    nom_departamento: str

    id: int | None = Field(default = None, primary_key = True)
    empleado: Optional["Empleado"] = Relationship(back_populates = "departamentos")