from sqlmodel import SQLModel

class DepartamentoCreate(SQLModel):
     empleado_id: int
     nom_departamento: str

class DepartamentoResponse():
     id: int

class DepartamentoUpdate(SQLModel):
     nom_departamento: str