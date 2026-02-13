from pydantic_settings import BaseSettings

class Config(BaseSettings):
    database_url: str = ""   #Falta la ruta a la base de datos y la DB
    debug: bool = False

    class Config:
        env_file = ".env"

config = Config()