import sys, os
p = os.path.abspath('.')
sys.path.insert(1, p)

from models.base.base_model import base_model

class licores(base_model):

    nombre: str
    cantidad: str
    grado_alcohol: str
    precio: str