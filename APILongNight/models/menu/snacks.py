import sys, os
p = os.path.abspath('.')
sys.path.insert(1, p)

#importar el modelo base
from models.base.base_model import base_model

class snacks(base_model):

    nombre: str
    cantidad: str
    precio: float
