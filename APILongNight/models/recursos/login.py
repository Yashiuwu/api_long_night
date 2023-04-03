from pydantic import BaseModel

class login(BaseModel):

    nombre_usario: str
    password: str