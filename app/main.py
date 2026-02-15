from fastapi import FastAPI
from app.routers import departamentoRout, empleadoRout
from app.db.session import engine
from sqlmodel import SQLModel

from fastapi.responses import Response

from fastapi.staticfiles import StaticFiles


app = FastAPI()

# Registrar las rutas
app.include_router(departamentoRout.router)
app.include_router(empleadoRout.router)

app.mount("/media", StaticFiles(directory="app/media"), name="media")

# Crear tablas en la base de datos si no existen
def init_db():
    try:
        print("Inicio de tablas ... ")
        SQLModel.metadata.create_all(engine)
        print("--> Se crearon correctamente. OK!")
    except Exception as e:
        print("Ocurrio un error al crear las tablas:", e)

init_db()

@app.get("/")
def root():
    return {"status": "API funcionando"}




@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204)

# Lanzar desde raíz de proyecto ( uvicorn app.main:app  ) 