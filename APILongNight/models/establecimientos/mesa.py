import sys, os
p = os.path.abspath('.')
sys.path.insert(1, p)

#imports de modelos 
from models.base.base_model import base_model

class mesa(base_model):

    numero_mesa: int
    numero_lugares: int
    tipo_mesa: str
    ocupada: bool
