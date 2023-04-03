import sys, os
p = os.path.abspath('.')
sys.path.insert(1, p)

#importacion del modelo base
from models.base.base_model import base_model
from models.menu.ingredientes import ingredientes

class platillos(base_model):

    nombre: str
    porcion: str
    ingrediente: list[ingredientes]
    precio: float